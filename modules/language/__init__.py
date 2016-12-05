"""
Handles updating the language using the online lmtool.

This class provides methods to check if the corpus has changed, and to
update the language to match the new corpus using the lmtool.  This allows
us to automatically update the language if the corpus has changed, saving
the user from having to do this manually.
"""

import logging
logger = logging.getLogger(__name__)


import re
import urllib.request, urllib.parse, urllib.error

import requests


def create_strings_file(path, source={}):
    # Open Strings File
    with open(path, 'w+') as strings:
        # Add Command Words To The Corpus
        for cmd in source:
            strings.write(cmd.strip().replace('%d', '') + "\n")
    

def create_sphinx_files(source, lm_path, dic_path):
    """Update the language using the online lmtool"""
    logger.debug("\x1b[32mUpdating Language\x1b[0m")

    host = 'http://www.speech.cs.cmu.edu'
    url = host + '/cgi-bin/tools/lmtool/run'

    # SUBMIT THE CORPUS TO THE LMTOOL
    response_text = ""
    with open(source, 'rb') as corpus:
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

    _download_file(lm_url, lm_path)
    _download_file(dic_url, dic_path)


def _download_file(url, dest):
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(dest, 'wb') as f:
            for chunk in r:
                f.write(chunk)