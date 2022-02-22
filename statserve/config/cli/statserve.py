statserve_cli = {
    "name": "StatServe",
    "description": "GRPCIO server utilizing the StatsStream library to provide streaming statistical computation as a service.",
    "arguments": [
        {
            "map_name": "server_config",
            "data_type": "dict",
            "arg_name": "--server-config-filepath",
            "var_name": "server_config_filepath",
            "arg_type": "file",
            "default": "OS_CWD",
            "default_filename": "server.json",
            "required": False,
            "help": "Path to a JSON config file containing  configuration data for the Statserve server (port, host, etc.)."
        },
        {
            "map_name": "log_level",
            "data_type": "string",
            "arg_name": "--log-level",
            "var_name": "log_level",
            "arg_type": "value",
            "default": "info",
            "required": False,
            "help": "Sets the log level."
        },
        {
            "map_name": "about",
            "data_type": "boolean",
            "arg_name": "--about",
            "var_name": "about",
            "arg_type": "flag",
            "required": False,
            "help": "Describes package version, package description, and lists all args."
        }
    ],
    "config_maps": [
        {
            "map_name": "server_config",
            "map_type": "value"
        },
        {
            "map_name": "log_level",
            "map_type": "value"
        },
        {
            "map_name": "about",
            "map_type": "value"
        }
    ],
    "attributes": [
        {
            "name": "server_config",
            "type": "dict",
            "default": {}
        },
        {
            "name": "log_level",
            "type": "string",
            "default": "info"
        },
        {
            "name": "about",
            "type": "boolean",
            "default": False
        }
    ]
}