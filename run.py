# OpenAssistant 0.04
# 2016 General Public License V3
# By Andrew Vavrek, Clayton G. Hobbs, Jezra

import signal

from gi.repository import GObject

from core import Assistant


if __name__ == '__main__':

    # Create Assistant
    a = Assistant()

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
