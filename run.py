# OpenAssistant 0.04
# 2016 General Public License V3
# By Andrew Vavrek, Clayton G. Hobbs, Jezra

from argparse import ArgumentParser, Namespace

import signal

from gi.repository import GObject

from core import Config, Assistant


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



if __name__ == '__main__':
    
    import sys
    
    opts = _parser(sys.argv[1:])
    conf = Config(path=opts.mind_dir)
    conf.options.update(vars(opts))

    a = Assistant(config=conf)

    # Initialize Gobject Threads
    GObject.threads_init()

    # Create Main Loop
    main_loop = GObject.MainLoop()

    # Handle Signal Interrupts
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    # Run Assistant
    a.run()

    # Start Main Loop
    try:
        main_loop.run()

    except:
        main_loop.quit()
        sys.exit()
        
