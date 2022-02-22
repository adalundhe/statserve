import grpc
import os
import asyncio
import uvloop
uvloop.install()
from zebra_automate_logging import Logger
from concurrent import futures
from .service import StreamServicer
from .service.proto import (
    add_StatStreamServerServicer_to_server
)


class Server:

    def __init__(self, streams=None, config=None):
        logger = Logger()
        self.session_logger = logger.generate_logger('statserve-server')
        self.port = config.get(
            'port', 
            os.getenv(
                'STATSERVE_SERVER_PORT',
                9001
            )
        )

        self.session_logger.debug('Connected to port: {port}'.format(port=self.port))

        self.server = grpc.aio.server()
        add_StatStreamServerServicer_to_server(
            StreamServicer(
                streams=streams
            ),
            self.server
        )

        self.loop = asyncio.get_event_loop()

    def start(self, blocking=True):
        server_address = '[::]:{port}'.format(port=self.port)
        self.session_logger.info('Statserve serving at address: {address}'.format(address=server_address))
        self.server.add_insecure_port(server_address)
        
        self.loop.run_until_complete(self._start(blocking))

    async def _start(self, blocking):
        await self.server.start()

        if blocking:
            await self.server.wait_for_termination()

    def stop(self):
        self.loop.run_until_complete(self.server.stop(0))
        
