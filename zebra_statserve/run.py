from .server import Server
from .command_line import CommandLine
from zebra_automate_logging import Logger

command_line = CommandLine()
stream = None
server = None

def run():
    command_line.get_custom_config()
    logger = Logger()
    logger.setup(command_line.log_level)
    logger.generate_logger('statserve-server')
    server = Server(
        streams=command_line.streams,
        config=command_line.server_config
    )
    server.start()

def stop():
    if server:
        server.stop()