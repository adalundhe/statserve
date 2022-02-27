from .proto import (
    StatStreamUpdate,
    StatStreamResponse,
    StatStreamQuery,
    StatStreamFieldQuery,
    StatStreamSummary,
    StatStreamFieldSummary,
    StatStreamServerServicer,
    StatStreamServerStub,
    StatStreamServer,
    Stream
)
from google.protobuf.json_format import (
    MessageToDict
)
from statstream.streaming import StatStreamGroup
from statstream.models import (
    Event,
    Query,
    StreamConfig
)
from easy_logger import Logger


class StreamServicer(StatStreamServerServicer):

    def __init__(self, streams=None):
        logger = Logger()
        self.session_logger = logger.generate_logger('statserve-server')

        self.stream = StatStreamGroup(
            streams=streams
        )

        super().__init__()

    async def AddStream(self, new_stream, context):
        self.session_logger.debug('Recieved new stream - {stream_name}'.format(
            stream_name=new_stream.stream_name
        ))

        self.session_logger.debug(
            'NEW STREAM: {stream}'.format(
                stream=MessageToDict(new_stream)
            )
        )

        stream = StreamConfig(MessageToDict(new_stream))
        await self.stream.add_stream(stream)
        response = StatStreamResponse(
            message="Added stream {stream_name}".format(
                stream_name=new_stream.stream_name
            )
        )

        self.session_logger.debug('Successfully added new stream - {stream_name}'.format(
            stream_name=new_stream.stream_name
        ))
        return response

    async def UpdateStats(self, update, context):
        self.session_logger.debug('Recieved new event - {key}:{value}'.format(
            key=update.key,
            value=update.value
        ))

        event = Event(MessageToDict(update))
        response_data = await self.stream.update(event)

        response = StatStreamResponse(
            field=response_data.get('field'),
            message=response_data.get('message')
        )

        self.session_logger.debug('Successfully stored new for - {field}'.format(
            field=response.field
        ))

        return response

    async def UpdateStatsStreaming(self, updates, context):
        async for update in updates:
            self.session_logger.debug('Recieved new event - {key}:{value}'.format(
                key=update.key,
                value=update.value
            ))

            event = Event(MessageToDict(update))
            response_data = await self.stream.update(event)

            response = StatStreamResponse(
                field=response_data.get('field'),
                message=response_data.get('message')
            )

            self.session_logger.debug('Successfully stored new for - {field}'.format(
                field=response.field
            ))
            yield response

    async def GetStreamStats(self, stat_query, context):
        self.session_logger.debug('Retrieving stats for stream - {stream}'.format(
            stream=stat_query.stream_name
        ))

        query = Query(MessageToDict(stat_query))

        stream_stats = await self.stream.get_stream_stats(query)

        summary = StatStreamSummary(
            stream_name=query.stream_name
        )

        summary.field_stats.update(stream_stats)
        
        self.session_logger.debug('Successfully retrieved stats for stream - {stream}'.format(
            stream=summary.stream_name
        ))

        return summary


    async def GetFieldStats(self, stat_query, context):
        self.session_logger.debug('Retrieving stats for stream - {stream} - on field - {field}'.format(
            stream=stat_query.stream_name,
            field=stat_query.key
        ))

        query = Query(MessageToDict(stat_query))
        field_stats = await self.stream.get_field_stats(query)

        summary = StatStreamFieldSummary(
            stream_name=query.stream_name
        )
        summary.metadata.update(field_stats.get('metadata'))
        summary.stats.update(field_stats.get('stats'))
        summary.counts.update(field_stats.get('counts'))
        summary.quantiles.update(field_stats.get('quantiles'))

        self.session_logger.debug('Successfully retrieved stats for stream - {stream} - on field - {field}'.format(
            stream=summary.stream_name,
            field=stat_query.key
        ))

        return summary

    async def GetFieldStat(self, stat_query, context):
        self.session_logger.debug('Retrieving stat - {stat} - for stream - {stream} - on field - {field}'.format(
            stream=stat_query.stream_name,
            field=stat_query.key,
            stat=stat_query.stat
        ))

        query = Query(MessageToDict(stat_query))

        field_stat = await self.stream.get_field_stat(query)

        summary = StatStreamFieldSummary(
            stream_name=query.stream_name
        )
        summary.metadata.update(field_stat.get('metadata'))
        summary.stats.update(field_stat.get('stats', {}))
        summary.counts.update(field_stat.get('counts', {}))
        summary.quantiles.update(field_stat.get('quantiles', {}))

        self.session_logger.debug('Successfully retrieved stat - {stat} - for stream - {stream} - on field - {field}'.format(
            stream=summary.stream_name,
            field=stat_query.key,
            stat=stat_query.stat
        ))
        return summary