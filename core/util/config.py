import os
import json

import logging
logger = logging.getLogger(__name__)

class Config:
    """OPEN ASSISTANT CONFIGURATION"""

    def __init__(self, path=None, **opts):
        logger.info("Configuration")
        
        # DIRECTORIES
        self.cache_dir = os.path.join(path, 'cache')
        self.conf_dir = os.path.join(path, 'conf')
        self.data_dir = os.path.join(path, 'words')
        self.img_dir = os.path.join(path, 'images')

        # CONFIGURATION FILES
        self.opt_file = os.path.join(self.conf_dir, "commands.json")

        # CACHE FILES
        self.history_file = os.path.join(self.cache_dir, "history")
        self.hash_file = os.path.join(self.cache_dir, "hash.json")

        # LANGUAGE FILES
        self.strings_file = os.path.join(self.cache_dir, "sentences.corpus")
        self.lang_file = os.path.join(self.cache_dir, 'lm')
        self.dic_file = os.path.join(self.cache_dir, 'dic')

        self._make_dir(self.conf_dir)
        self._make_dir(self.cache_dir)
        self._make_dir(self.data_dir)
        
        self.options = self._read_options_file()
        self.commands = None
        #self.create_strings_file()


    def _make_dir(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)


    def _read_options_file(self):
        try:
            with open(self.opt_file, 'r') as f:
                _options = json.load(f)
                return _options
        except FileNotFoundError:
            # MAKE AN EMPTY OPTIONS NAMESPACE
            print("No options file found: %s".format(self.opt_file))
            return {}


    def create_strings_file(self):
        # Open Strings File
        with open(self.strings_file, 'w') as strings:
            # Add Command Words To The Corpus
            for voice_cmd in sorted(self.options.commands.keys()):
                strings.write(voice_cmd.strip().replace('%d', '') + "\n")
            # Add Number Words To The Corpus
            for word in self.number_parser.number_words:
                strings.write(word + " ")
            strings.write("\n")


    #def update_voice_commands_if_changed(self):
    #   """USE HASHES TO TEST IF THE VOICE COMMANDS HAVE CHANGED"""
       #stored_hash = self.hasher['voice_commands']

       # Calculate The Hash The Voice Commands Have Right Now
       #hasher = self.hasher.get_hash_object()
       #for voice_cmd in self.commands.keys():
        #   hasher.update(voice_cmd.encode('utf-8'))
           # Add A Separator To Avoid Odd Behavior
        #   hasher.update('\n'.encode('utf-8'))
       #new_hash = hasher.hexdigest()

       #if new_hash != stored_hash:
    #   self.create_strings_file()
           #self.hasher['voice_commands'] = new_hash
           #self.hasher.store()