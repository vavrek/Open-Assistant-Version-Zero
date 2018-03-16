import logging
logger = logging.getLogger(__name__)


import re
import urllib.request, urllib.parse, urllib.error

import requests

#from .hasher import Hasher

NET_TEST_SERVER = "http://www.speech.cs.cmu.edu"


class LanguageUpdater:
    """
    Handles updating the language using the online lmtool.

    This class provides methods to check if the corpus has changed, and to
    update the language to match the new corpus using the lmtool.  This allows
    us to automatically update the language if the corpus has changed, saving
    the user from having to do this manually.
    """

    def __init__(self, config):
        self.config = config
        self.create_strings_file()

        #self.hasher = Hasher(config)

    # def update_language_if_changed(self):
    #     """TEST IF THE LANGUAGE HAS CHANGED"""
    #     if self.language_has_changed():
    #         """TEST NET CONNECTION AND UPDATE IF CONNECTED"""
    #         try:
    #           response=urllib.request.urlopen(NET_TEST_SERVER,timeout=1)
    #           print ("OpenAssistant: \x1b[32mNetwork Connection Established\x1b[0m")
    #           self.update_language()
    #           self.save_language_hash()
    #         except urllib.error.URLError as e: pass
    #         print ("OpenAssistant: \x1b[31mNo Network Connection\x1b[0m")
    #
    # def language_has_changed(self):
    #     """Use hashes to test if the language has changed"""
    #     self.stored_hash = self.hasher['language']
    #
    #     # CALCULATE LANGUAGE FILE HASH
    #     hasher = self.hasher.get_hash_object()
    #     with open(self.config.strings_file, 'rb') as sfile:
    #         buf = sfile.read()
    #         hasher.update(buf)
    #     self.new_hash = hasher.hexdigest()
    #
    #     return self.new_hash != self.stored_hash


    # def create_strings_file(path, source={}):
    def create_strings_file(self):
        # Open Strings File
        # with open(path, 'w+') as strings:
        with open(self.config.strings_file, 'w') as strings:
            # Add Command Words To The Corpus
            # for cmd in source:
            #     strings.write(cmd.strip().replace('%d', '') + "\n")
            for voice_cmd in sorted(self.config.commands.keys()):
                strings.write(voice_cmd.strip().replace('%d', '') + "\n")

    # def create_sphinx_files(source, lm_path, dic_path):
    #     """Update the language using the online lmtool"""
    #     logger.debug("\x1b[32mUpdating Language\x1b[0m")
    #
    #     host = 'http://www.speech.cs.cmu.edu'
    #     url = host + '/cgi-bin/tools/lmtool/run'
    #
    #     # SUBMIT THE CORPUS TO THE LMTOOL
    #     response_text = ""
    #     with open(source, 'rb') as corpus:
    #         files = {'corpus': corpus}
    #         values = {'formtype': 'simple'}
    #
    #         r = requests.post(url, files=files, data=values)
    #         response_text = r.text
    #
    #     # PARSE RESPONSE TO GET URLS OF THE FILES WE NEED
    #     path_re = r'.*<title>Index of (.*?)</title>.*'
    #     number_re = r'.*TAR([0-9]*?)\.tgz.*'
    #     for line in response_text.split('\n'):
    #         # ERROR RESPONSE
    #         if "[_ERRO_]" in line:
    #             return 1
    #         # IF WE FOUND THE DIRECTORY, KEEP IT AND DON'T BREAK
    #         if re.search(path_re, line):
    #             path = host + re.sub(path_re, r'\1', line)
    #         # IF WE FOUND THE NUMBER, KEEP IT AND BREAK
    #         elif re.search(number_re, line):
    #             number = re.sub(number_re, r'\1', line)
    #             break
    #
    #     lm_url = path + '/' + number + '.lm'
    #     dic_url = path + '/' + number + '.dic'
    #
    #     _download_file(lm_url, lm_path)
    #     _download_file(dic_url, dic_path)

    def update_language(self):
        """Update the language using the online lmtool"""
        logger.debug("\x1b[32mUpdating Language\x1b[0m")

        host = 'http://www.speech.cs.cmu.edu'
        url = host + '/cgi-bin/tools/lmtool/run'

        # SUBMIT THE CORPUS TO THE LMTOOL
        response_text = ""
        with open(self.config.strings_file, 'rb') as corpus:
            files = {'corpus': corpus}
            values = {'formtype': 'simple'}

            r = requests.post(url, files=files, data=values)
            response_text = r.text

        # PARSE RESPONSE TO GET URLS OF THE FILES WE NEED
        path_re = r'.*<title>Index of (.*?)</title>.*'
        number_re = r'.*TAR([0-9]*?)\.tgz.*'
        for line in response_text.split('\n'):
            # ERROR RESPONSE
            if "[_ERRO_]" in line:
                return 1
            # IF WE FOUND THE DIRECTORY, KEEP IT AND DON'T BREAK
            if re.search(path_re, line):
                path = host + re.sub(path_re, r'\1', line)
            # IF WE FOUND THE NUMBER, KEEP IT AND BREAK
            elif re.search(number_re, line):
                number = re.sub(number_re, r'\1', line)
                break

        lm_url = path + '/' + number + '.lm'
        dic_url = path + '/' + number + '.dic'

        if self.config.lang_file is not None:
            self._download_file(lm_url, self.config.lang_file)
        self._download_file(dic_url, self.config.dic_file)

    # def save_language_hash(self):
    #     self.hasher['language'] = self.new_hash
    #     self.hasher.store()

    def _download_file(self, url, path):
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open(path, 'wb') as f:
                for chunk in r:
                    f.write(chunk)

    # def _download_file(url, dest):
    #     r = requests.get(url, stream=True)
    #     if r.status_code == 200:
    #         with open(dest, 'wb') as f:
    #             for chunk in r:
    #                 f.write(chunk)
