# core.py - Open Assistant System Core

import os
import sys
import subprocess

# import pyaudio
# import math
# import audioop

from .recognizer import Recognizer
from .utilities import Config, Hasher, LanguageUpdater


class Assistant:

    def __init__(self):
        self.options = {}
        self.continuous_listen = True

        # Load configuration
        self.config = Config()
        self.options = vars(self.config.options)
        self.commands = self.options['commands']

        # Create hasher
        self.hasher = Hasher(self.config)

        # Create Strings File
        self.update_voice_commands_if_changed()
        
        # Optional: history
        if self.options['history']:
            self.history = []

        # Update language model if changed
        self.language_updater = LanguageUpdater(self.config)
        self.language_updater.update_language_if_changed()

        # Create recognizer
        self.recognizer = Recognizer(self.config)
        self.recognizer.connect('finished', self.recognizer_finished)

    def update_voice_commands_if_changed(self):
        """Use hashes to detect if the commands have changed"""
        stored_hash = self.hasher['voice_commands']

        # Calculate the current commands hash
        hasher = self.hasher.get_hash_object()
        for voice_cmd in self.commands.keys():
            hasher.update(voice_cmd.encode('utf-8'))
            # Add a separator to avoid odd behavior
            hasher.update('\n'.encode('utf-8'))
        new_hash = hasher.hexdigest()

        if new_hash != stored_hash:
            self.create_strings_file()
            self.hasher['voice_commands'] = new_hash
            self.hasher.store()


    """ def setup_mic(self, num_samples=50):
        # Gets average audio intensity of your mic sound. You can use it to get
        #    average intensities while you're talking and/or silent. The average
        #    is the avg of the .2 of the largest intensities recorded.
        
        # Microphone stream config.
        self.CHUNK = 1024  # CHUNKS of bytes to read each time from mic
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 16000

        self.SILENCE_LIMIT = 1  # Silence limit in seconds. The max ammount of seconds where
                           # only silence is recorded. When this time passes the
                           # recording finishes and the file is decoded

        self.PREV_AUDIO = 0.5  # Previous audio (in seconds) to prepend. When noise
                          # is detected, how much of previously recorded audio is
                          # prepended. This helps to prevent chopping the beginning
                          # of the phrase.

        self.THRESHOLD = 4500
        self.num_phrases = -1

        print ("Getting intensity values from mic.")
        p = pyaudio.PyAudio()
        stream = p.open(format=self.FORMAT, 
                        channels=self.CHANNELS,
                        rate=self.RATE, 
                        input=True, 
                        frames_per_buffer=self.CHUNK)

        values = [math.sqrt(abs(audioop.avg(stream.read(self.CHUNK), 4)))
                  for x in range(num_samples)]
        values = sorted(values, reverse=True)
        r = sum(values[:int(num_samples * 0.2)]) / int(num_samples * 0.2)
        print (" Finished ")
        print (" Average audio intensity is ", r)
        stream.close()
        p.terminate()

        if r < 3000:
            self.THRESHOLD = 3500
        else:
            self.THRESHOLD = r + 100
        """

    def create_strings_file(self):
        # Open strings file
        with open(self.config.strings_file, 'w') as strings:
            # Add command words to the corpus
            for voice_cmd in sorted(self.commands.keys()):
                strings.write(voice_cmd.strip().replace('%d', '') + "\n")

    def log_history(self, text):
        if self.options['history']:
            self.history.append(text)
            if len(self.history) > self.options['history']:
                # Pop off first item
                self.history.pop(0)

            # Open And Truncate History File
            with open(self.config.history_file, 'w') as hfile:
                for line in self.history:
                    hfile.write(line + '\n')

    def run_command(self, cmd):
        """Print command and run"""
        print("\x1b[32m< ! >\x1b[0m", cmd)
        self.recognizer.pause()
        os.system(cmd)
        #subprocess.call(cmd, shell=True)
        self.recognizer.listen()

    def recognizer_finished(self, recognizer, text):
        t = text.lower()

        # Test for a matching command
        if t in self.commands:
            # Run the 'valid_sentence_command' if set
            os.system('clear')
            print("Open Assistant: \x1b[32mListening\x1b[0m")
            if self.options['valid_sentence_command']:
                os.system(self.options['valid_sentence_command'])
                #subprocess.call(self.options['valid_sentence_command'],
                                #shell=True)
            cmd = self.commands[t]

            # Should we be passing words?
            os.system('clear')
            print("Open Assistant: \x1b[32mListening\x1b[0m")
            if self.options['pass_words']:
                cmd += " " + t
            print("\x1b[32m< ! >\x1b[0m {0}".format(t))
            self.run_command(cmd)
            self.log_history(text)
        
        else:
            # Run the invalid_sentence_command if set
            if self.options['invalid_sentence_command']:
                subprocess.call(self.options['invalid_sentence_command'],
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
