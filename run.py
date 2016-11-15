# OpenAssistant 0.04
# 2016 General Public License V3
# By Andrew Vavrek, Clayton G. Hobbs, Jezra

from argparse import ArgumentParser, Namespace
import logging
#import signal
import sys

#from gi.repository import GObject

from core import Config, Assistant
#from core.numbers import NumberParser
#from core.recognizer import Recognizer
#from core.util.hasher import Hasher
#from core.util.language_updater import LanguageUpdater


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)    


def _parser(args):
    parser = ArgumentParser()

    parser.add_argument("-c", "--continuous",
            action="store_true", dest="continuous", default=False,
            help="Start interface with 'continuous' listen enabled")

    parser.add_argument("-p", "--pass-words",
            action="store_true", dest="pass_words", default=False,
            help="Pass the recognized words as arguments to the shell" +
            " command")

    parser.add_argument("-H", "--history", type=int,
            action="store", dest="history",
            help="Number of commands to store in history file")

    parser.add_argument("-m", "--microphone", type=int,
            action="store", dest="microphone", default=None,
            help="Audio input card to use (if other than system default)")

    parser.add_argument("--valid-sentence-command", type=str,
            dest="valid_sentence_command", action='store',
            help="Command to run when a valid sentence is detected")

    parser.add_argument("--invalid-sentence-command", type=str,
            dest="invalid_sentence_command", action='store',
            help="Command to run when an invalid sentence is detected")
            
    parser.add_argument("-M", "--mind", type=str,
            dest="mind_dir", action='store',
            help="Path to mind to use for assistant")

    return parser.parse_args(args)


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




if __name__ == '__main__':
    
    # Parse command-line options,
    #  use `Config` to load mind configuration
    #  command-line overrides config file
    args = _parser(sys.argv[1:])
    logger.debug("Arguments: {args}".format(args=args))
    conf = Config(path=args.mind_dir, **vars(args))


    # A configured Assistant
    a = Assistant(config=conf)
    
    
    #
    # Further patching to ease transition..
    #
    # Create Hasher
    #self.hasher = Hasher(self.config)
    
    # Create Strings File
    #self.update_voice_commands_if_changed()
    #self.number_parser = NumberParser()
    
    # Add Number Words To The Corpus
    #for word in self.number_parser.number_words:
    #    strings.write(word + " ")
    #strings.write("\n")

    # Update Language If Changed
    #self.language_updater = LanguageUpdater(self.config)
    #self.language_updater.update_language_if_changed()

    # Create Recognizer
    #self.recognizer = Recognizer(self.config)
    #recognizer = Recognizer(config)
    #self.recognizer.connect('finished', self.recognizer_finished)
    #recognizer.connect('finished', recognizer_finished)
    #
    # End patching
    #
    
    
    #
    # Questionable dependencies
    #
    # Initialize Gobject Threads
    #GObject.threads_init()

    # Create Main Loop
    #main_loop = GObject.MainLoop()

    # Handle Signal Interrupts
    #signal.signal(signal.SIGINT, signal.SIG_DFL)
    #
    # End Questionable dependencies
    #

    # Run Assistant
    #  maybe use threading module?
    #  could supplant GObject features
    #a.run()
    #recognizer.listen()
    

    # Start Main Loop
    #try:
    #    main_loop.run()

    #except Exception as e:
    #    print(e)
    #    main_loop.quit()
    #    sys.exit()
        
