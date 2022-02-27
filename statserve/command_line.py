from pycli_tools import BaseConfig
from importlib.metadata import version
from .config.cli.statserve import statserve_cli

class CommandLine(BaseConfig):

    def __init__(self):
        super(CommandLine, self).__init__(cli=statserve_cli, package_version=version('statserve'))
        self.streams = []
        self.server_config = {}
        self.log_level = 'info'

    def get_custom_config(self):
        self.config_helper.setup()
        self.config_helper.set_cli()
        self.config_helper.parse_cli()

        if self.config_helper["about"] == True:
            print(self.config_helper.generate_help_string())
            exit(0)


        self.server_config = self.config_helper['server_config']
        self.streams = self.server_config.get('streams')
        self.log_level = self.config_helper['log_level']
