import grpc
import os
import uvloop
uvloop.install()
from easy_logger import Logger
from google.protobuf.json_format import (
    MessageToDict
)
from .service.proto import (
    StatStreamUpdate,
    StatStreamQuery,
    StatStreamFieldQuery,
    Stream,
    StatStreamServerStub
)
from .utils import connect_with_retry
from async_tools.datatypes import AsyncList


class StatServeClient:

    def __init__(self, config=None):
        logger = Logger()
        self.session_logger = logger.generate_logger('statserve-server')

        host = config.get(
            'host', 
            os.getenv(
                'STATSERVE_SERVER_HOST',
                'localhost'
            )
        )
        port = config.get(
            'port', 
            os.getenv(
                'STATSERVE_SERVE_PORT',
                9001
            )
        )

        host_string = '{host}:{port}'.format(
            host=host,
            port=port
        )

        self.session_logger.debug('Connecting to: {host_string}'.format(host_string=host_string))
        
        self.channel = grpc.aio.insecure_channel(host_string)
        self.service = StatStreamServerStub(self.channel)
        self.stream_name = None

    @connect_with_retry(timeout_threshold=15)
    async def register(self, new_stream):
        if self.stream_name is None:
            self.stream_name = new_stream.get('stream_name')
            
        self.session_logger.debug('Registering stream - {stream_name}'.format(
            stream_name=self.stream_name
        ))
        stream = Stream(
            stream_name=self.stream_name
        )
        
        stream.fields.update(new_stream.get('fields', {}))

        response = await self.service.AddStream(stream)

        self.session_logger.debug('Successfully registered stream - {stream_name}'.format(
            stream_name=self.stream_name
        ))
        return MessageToDict(response)

    @connect_with_retry(timeout_threshold=15)
    async def update(self, event):
        stream_name = event.get('stream_name') 
        if stream_name is None:
            stream_name = self.stream_name

        self.session_logger.debug('Submitting event - {key}:{value}'.format(
            key=event.get('key'),
            value=event.get('value')
        ))
        stream_update = StatStreamUpdate(
            stream_name=stream_name,
            key=event.get('key'),
            value=event.get('value'),
            bin=event.get('bin')
        )

        stream_update.metadata.update(event.get('metadata', {}))

        response = await self.service.UpdateStats(stream_update)

        self.session_logger.debug('Successfully submitted event - {key}:{value}'.format(
            key=event.get('key'),
            value=event.get('value')
        ))

        return MessageToDict(response)
        

    @connect_with_retry(timeout_threshold=15)
    async def stream_update(self, events):
        stream_updates = []
        for event in events:
            stream_name = event.get('stream_name') 
            if stream_name is None:
                stream_name = self.stream_name

            self.session_logger.debug('Submitting event - {key}:{value}'.format(
                key=event.get('key'),
                value=event.get('value')
            ))
            stream_update = StatStreamUpdate(
                stream_name=stream_name,
                key=event.get('key'),
                value=event.get('value'),
                bin=event.get('bin')
            )

            stream_update.metadata.update(event.get('metadata', {}))
            stream_updates += [stream_update]

        async for response in self.service.UpdateStatsStreaming(AsyncList(stream_updates)):
            self.session_logger.debug('Successfully submitted event - {key}:{value}'.format(
                key=event.get('key'),
                value=event.get('value')
            ))
            
            yield MessageToDict(response)


    @connect_with_retry(timeout_threshold=15)
    async def get_stream_stats(self, query):
        stream_name = query.get('stream_name')
        if stream_name is None:
            stream_name = self.stream_name

        self.session_logger.debug('Retrieving summary for stream - {stream}'.format(
            stream=stream_name
        ))

        query = StatStreamQuery(
            stream_name=stream_name
        )

        response = await self.service.GetStreamStats(query)

        self.session_logger.debug('Successfully retrieved summary for stream - {stream}'.format(
            stream=stream_name
        ))

        return MessageToDict(response)

    @connect_with_retry(timeout_threshold=15)
    async def get_field_stats(self, query):
        stream_name = query.get('stream_name') 
        if stream_name is None:
            stream_name = self.stream_name

        field_name = query.get('key')

        self.session_logger.debug('Retrieving summary for stream - {stream} - and field - {field}'.format(
            stream=stream_name,
            field=field_name
        ))

        query = StatStreamFieldQuery(
            stream_name=stream_name,
            key=field_name
        )
        response = await self.service.GetFieldStats(query)

        self.session_logger.debug('Successfully retrieved summary for stream - {stream} - and field - {field}'.format(
            stream=stream_name,
            field=field_name
        ))

        return MessageToDict(response)

    @connect_with_retry(timeout_threshold=15)
    async def get_field_stat(self, query):
        stream_name = query.get('stream_name') 
        if stream_name is None:
            stream_name = self.stream_name

        field_name = query.get('key')
        stat_type = query.get('type')
        stat_name = query.get('stat')

        self.session_logger.debug('Retrieving stat - {stat} - for stream - {stream} - and field - {field}'.format(
            stat=stat_name,
            stream=stream_name,
            field=field_name
        ))

        query = StatStreamFieldQuery(
            stream_name=stream_name,
            key=field_name,
            type=stat_type,
            stat=stat_name
        )

        response = await self.service.GetFieldStat(query)

        self.session_logger.debug('Successfully retrieved stat - {stat} - for stream - {stream} - and field - {field}'.format(
            stat=stat_name,
            stream=stream_name,
            field=field_name
        ))

        return MessageToDict(response)
