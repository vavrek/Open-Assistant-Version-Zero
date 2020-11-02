# oa.py - Core Open Assistant Loop

import signal
from gi.repository import GObject
from core import Assistant

if __name__ == '__main__':
    # Create Assistant
    a = Assistant()

    # Create Main Loop
    main_loop = GObject.MainLoop()

    # Handle Signal Interrupts
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    # Run Assistant
    # a.setup_mic()
    a.run()

    # Start Main Loop
    try:
        main_loop.run()

    except:
        main_loop.quit()
        sys.exit()
        
