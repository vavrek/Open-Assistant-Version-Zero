# OpenAssistant 0.04
# 2016 General Public License V3
# By Andrew Vavrek, Clayton G. Hobbs, Jezra, Jonathan Kulp

# utilities.py - System Utilities

import os
import re
import json
import hashlib
import urllib.request, urllib.parse, urllib.error

from argparse import ArgumentParser, Namespace

import requests


NET_TEST_SERVER = "http://www.speech.cs.cmu.edu"


class Config:

    """OPEN ASSISTANT CONFIGURATION"""

    # DIRECTORIES
    mind_dir = os.environ['MINDDIR']
    
    conf_dir = os.path.join(mind_dir, 'words')
    cache_dir = os.path.join(mind_dir, 'words')
    data_dir = os.path.join(mind_dir, 'words')
    img_dir = os.path.join(mind_dir, 'images')

    # CONFIGURATION FILES
    opt_file = os.path.join(conf_dir, "commands.json")

    # CACHE FILES
    history_file = os.path.join(cache_dir, "history")
    hash_file = os.path.join(cache_dir, "hash.json")

    # DATA FILES
    strings_file = os.path.join(data_dir, "sentences.corpus")
    lang_file = os.path.join(data_dir, 'lm')
    dic_file = os.path.join(data_dir, 'dic')

    def __init__(self):
        # MAKE DIRECTORIES IF NEEDED
        self._make_dir(self.conf_dir)
        self._make_dir(self.cache_dir)
        self._make_dir(self.data_dir)

        # SET UP ARGUMENT PARSER
        self._parser = ArgumentParser()

        self._parser.add_argument("-c", "--continuous",
                action="store_true", dest="continuous", default=False,
                help="Start interface with 'continuous' listen enabled")

        self._parser.add_argument("-p", "--pass-words",
                action="store_true", dest="pass_words", default=False,
                help="Pass the recognized words as arguments to the shell" +
                " command")

        self._parser.add_argument("-H", "--history", type=int,
                action="store", dest="history",
                help="Number of commands to store in history file")

        self._parser.add_argument("-m", "--microphone", type=int,
                action="store", dest="microphone", default=None,
                help="Audio input card to use (if other than system default)")

        self._parser.add_argument("--valid-sentence-command", type=str,
                dest="valid_sentence_command", action='store',
                help="Command to run when a valid sentence is detected")

        self._parser.add_argument("--invalid-sentence-command", type=str,
                dest="invalid_sentence_command", action='store',
                help="Command to run when an invalid sentence is detected")

        # READ THE CONFIGURATION FILE
        self._read_options_file()

        # PARSE COMMAND-LINE ARGUMENTS, OVERRIDING CONFIG FILE AS APPROPRIATE
        self._parser.parse_args(namespace=self.options)

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


class Hasher:
    """Keep track of hashes"""

    def __init__(self, config):
        self.config = config
        try:
            with open(self.config.hash_file, 'r') as f:
                self.hashes = json.load(f)
        except IOError:
            # NO STORED HASH
            self.hashes = {}

    def __getitem__(self, hashname):
        try:
            return self.hashes[hashname]
        except (KeyError, TypeError):
            return None

    def __setitem__(self, hashname, value):
        self.hashes[hashname] = value

    def get_hash_object(self):
        """Returns an object to compute a new hash"""
        return hashlib.sha256()

    def store(self):
        """Store the current hashes into a the hash file"""
        with open(self.config.hash_file, 'w') as f:
            json.dump(self.hashes, f)


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
        self.hasher = Hasher(config)

    def update_language_if_changed(self):
        """TEST IF THE LANGUAGE HAS CHANGED"""
        if self.language_has_changed():
            """TEST NET CONNECTION AND UPDATE IF CONNECTED"""
            try:
              response=urllib.request.urlopen(NET_TEST_SERVER,timeout=1)
              print ("OpenAssistant: \x1b[32mNetwork Connection Established\x1b[0m")
              self.update_language()
              self.save_language_hash()
            except urllib.error.URLError as e: pass
            print ("OpenAssistant: \x1b[31mNo Network Connection\x1b[0m")

    def language_has_changed(self):
        """Use hashes to test if the language has changed"""
        self.stored_hash = self.hasher['language']

        # CALCULATE LANGUAGE FILE HASH
        hasher = self.hasher.get_hash_object()
        with open(self.config.strings_file, 'rb') as sfile:
            buf = sfile.read()
            hasher.update(buf)
        self.new_hash = hasher.hexdigest()

        return self.new_hash != self.stored_hash

    def update_language(self):
        """Update the language using the online lmtool"""
        print('OpenAssistant: \x1b[32mUpdating Commands\x1b[0m')

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

        self._download_file(lm_url, self.config.lang_file)
        self._download_file(dic_url, self.config.dic_file)

    def save_language_hash(self):
        self.hasher['language'] = self.new_hash
        self.hasher.store()

    def _download_file(self, url, path):
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open(path, 'wb') as f:
                for chunk in r:
                    f.write(chunk)
