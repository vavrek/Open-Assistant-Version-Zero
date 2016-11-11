# Open Assistant 0.03
# 2016 General Public License V3
# By Andrew Vavrek, Clayton G. Hobbs, Jezra, Jonathan Kulp

# core.py - Open Assistant System Core

import os
import sys
import subprocess

from .util.hasher import Hasher
from .util.language_updater import LanguageUpdater

from .recognizer import Recognizer
from .numbers import NumberParser


class Assistant:

    def __init__(self, config=None):
        self.config = config if config is not None else {}
        
        # Load Configuration
        #self.config = Config()
        #self.config.options = vars(self.config.options)
        self.commands = self.config.commands

        # Create Hasher
        #self.hasher = Hasher(self.config)

        # Create Strings File
        #self.update_voice_commands_if_changed()
        self.number_parser = NumberParser()
        
        # Optional: History
        self.history = []
        #if self.config['history']:
        #    self.history = []

        # Update Language If Changed
        #self.language_updater = LanguageUpdater(self.config)
        #self.language_updater.update_language_if_changed()

        # Create Recognizer
        self.recognizer = Recognizer(self.config)
        self.recognizer.connect('finished', self.recognizer_finished)

    #def update_voice_commands_if_changed(self):
    #    """USE HASHES TO TEST IF THE VOICE COMMANDS HAVE CHANGED"""
    #    stored_hash = self.hasher['voice_commands']

    #    # Calculate The Hash The Voice Commands Have Right Now
    #    hasher = self.hasher.get_hash_object()
    #    for voice_cmd in self.commands.keys():
    #        hasher.update(voice_cmd.encode('utf-8'))
    #        # Add A Separator To Avoid Odd Behavior
    #        hasher.update('\n'.encode('utf-8'))
    #    new_hash = hasher.hexdigest()

    #    if new_hash != stored_hash:
    #        self.create_strings_file()
    #        self.hasher['voice_commands'] = new_hash
    #        self.hasher.store()

    def log_history(self, text):
        if self.config.options['history']:
            self.history.append(text)
            if len(self.history) > self.config.options['history']:
                # Pop Off First Item
                self.history.pop(0)

            # Open And Truncate History File
            with open(self.config.history_file, 'w') as hfile:
                for line in self.history:
                    hfile.write(line + '\n')

    def run_command(self, cmd):
        """PRINT COMMAND AND RUN"""
        print("\x1b[32m< ! >\x1b[0m", cmd)
        self.recognizer.pause()
        subprocess.call(cmd, shell=True)
        self.recognizer.listen()

    def recognizer_finished(self, recognizer, text):
        t = text.lower()
        numt, nums = self.number_parser.parse_all_numbers(t)
        # Is There A Matching Command?
        if t in self.commands:
            # Run The 'valid_sentence_command' If It's Set
            os.system('clear')
            print("Open Assistant: \x1b[32mListening\x1b[0m")
            if self.config.options['valid_sentence_command']:
                subprocess.call(self.config.options['valid_sentence_command'],
                                shell=True)
            cmd = self.commands[t]
            # Should We Be Passing Words?
            os.system('clear')
            print("Open Assistant: \x1b[32mListening\x1b[0m")
            if self.config.options['pass_words']:
                cmd += " " + t
            print("\x1b[32m< ! >\x1b[0m {0}".format(t))
            self.run_command(cmd)
            self.log_history(text)
        elif numt in self.commands:
            # Run 'valid_sentence_command' Set
            os.system('clear')
            print("Open Assistant: \x1b[32mListening\x1b[0m")
            if self.config.options['valid_sentence_command']:
                subprocess.call(self.config.options['valid_sentence_command'],
                                shell=True)
            cmd = self.commands[numt]
            cmd = cmd.format(*nums)
            # Should We Be Passing Words?
            if self.config.options['pass_words']:
                cmd += " " + t
            print("\x1b[32m< ! >\x1b[0m {0}".format(t))
            self.run_command(cmd)
            self.log_history(text)
        else:
            # Run The Invalid_sentence_command If It's Set
            if self.config.options['invalid_sentence_command']:
                subprocess.call(self.config.options['invalid_sentence_command'],
                                shell=True)
            print("\x1b[31m< ? >\x1b[0m {0}".format(t))

    def run(self):
        self.recognizer.listen()

    def quit(self):
        sys.exit()

    def process_command(self, command):
        print(command)
        if command == "listen":
            self.recognizer.listen()
        elif command == "stop":
            self.recognizer.pause()
        elif command == "continuous_listen":
            self.continuous_listen = True
            self.recognizer.listen()
        elif command == "continuous_stop":
            self.continuous_listen = False
            self.recognizer.pause()
        elif command == "quit":
            self.quit()
