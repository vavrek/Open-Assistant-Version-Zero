import hashlib
import json


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