import os

class Config:
    """OPEN ASSISTANT CONFIGURATION"""

    def __init__(self, path=None):

        # DIRECTORIES
        self.conf_dir = os.path.join(path, 'etc')
        self.cache_dir = os.path.join(path, 'cache')
        self.data_dir = os.path.join(path, 'language')
        self.img_dir = os.path.join(path, 'img')

        # CONFIGURATION FILES
        self.opt_file = os.path.join(self.conf_dir, "commands.json")

        # CACHE FILES
        self.history_file = os.path.join(self.cache_dir, "history")
        self.hash_file = os.path.join(self.cache_dir, "hash.json")

        # LANGUAGE FILES
        self.strings_file = os.path.join(self.data_dir, "sentences.corpus")
        self.lang_file = os.path.join(self.data_dir, 'lm')
        self.dic_file = os.path.join(self.data_dir, 'dic')

        self._make_dir(self.conf_dir)
        self._make_dir(self.cache_dir)
        self._make_dir(self.data_dir)

    def _make_dir(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)

    def _read_options_file(self):
        try:
            with open(self.opt_file, 'r') as f:
                self.options = json.load(f)
                self.options = Namespace(**self.options)
        except FileNotFoundError: 
            # MAKE AN EMPTY OPTIONS NAMESPACE
            self.options = Namespace()

    def create_strings_file(self):
        # Open Strings File
        with open(self.strings_file, 'w') as strings:
            # Add Command Words To The Corpus
            for voice_cmd in sorted(self.commands.keys()):
                strings.write(voice_cmd.strip().replace('%d', '') + "\n")
            # Add Number Words To The Corpus
            for word in self.number_parser.number_words:
                strings.write(word + " ")
            strings.write("\n")
