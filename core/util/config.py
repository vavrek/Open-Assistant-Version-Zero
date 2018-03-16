import logging
logger = logging.getLogger(__name__)

import os
import json


class Config:
    """OPEN ASSISTANT CONFIGURATION"""

    def __init__(self, path=None, **opts):
        logger.info("Loading Mind: {path}".format(path=path))

        # DIRECTORIES
        self.cache_dir = os.path.join(path, 'cache')
        self.conf_dir = os.path.join(path, 'conf')

        # CONFIGURATION FILES
        self.opt_file = os.path.join(self.conf_dir, "settings.json")
        self.cmd_file = os.path.join(self.conf_dir, "commands.json")

        # CACHE FILES
        self.history_file = os.path.join(self.cache_dir, "history")
        self.hash_file = os.path.join(self.cache_dir, "hash.json")

        self._make_dir(self.conf_dir)
        self._make_dir(self.cache_dir)

        self.options = self._read_options_file()
        self.options.update(opts)
        logger.info("Options: {}".format(self.options))

        self.commands = self._read_commands_file()
        logger.info("Command Count: {}".format(len(self.commands)))


    def _make_dir(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)


    def _read_options_file(self):
        try:
            logger.debug("Reading options from {}".format(self.opt_file))
            with open(self.opt_file, 'r') as f:
                _options = json.load(f)
                return _options
        except FileNotFoundError:
            # MAKE AN EMPTY OPTIONS NAMESPACE
            logger.warn("Error reading options file: {path}".format(path=self.opt_file))
            return {}


    def _read_commands_file(self):
        try:
            logger.debug("Reading commands from {}".format(self.cmd_file))
            with open(self.cmd_file, 'r') as f:
                _cmds = json.load(f)
                return _cmds
        except FileNotFoundError:
            # MAKE AN EMPTY COMMANDS NAMESPACE
            logger.warn("Error reading commands file: {path}".format(path=self.cmd_file))
            return {}
