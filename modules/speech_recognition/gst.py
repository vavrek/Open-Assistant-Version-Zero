import logging
logger = logging.getLogger(__name__)

import gi
gi.require_version('Gst', '1.0')
from gi.repository import GObject, Gst
GObject.threads_init()
Gst.init(None)


logger.debug("Loading")
class Recognizer(GObject.GObject):
    __gsignals__ = {
        'finished' : (GObject.SIGNAL_RUN_LAST, GObject.TYPE_NONE,
                      (GObject.TYPE_STRING,))
    }

    def __init__(self, mic=None, dic_file=None, lm_file=None, fsg_file=None):
        GObject.GObject.__init__(self)
        logger.debug("Initializing Recognizer")

        # Configure Audio Source
        audio_src = 'autoaudiosrc' + ('' if mic is None else ' device="hw:{0},0"'.format(mic))

        # Build Pipeline
        cmd = (
            audio_src +
            ' ! audioconvert' +
            ' ! audioresample' +
            ' ! pocketsphinx {}'.format(' '.join([
                    '{}={}'.format(opt, val) for opt, val in [
                        ('dict', dic_file),
                        ('lm', lm_file), 
                        ('fsg', fsg_file)
                    ] if val is not None
                ])) +
            ' ! appsink sync=false'
        )
        logger.debug(cmd)
        
        try:
            self.pipeline = Gst.parse_launch(cmd)
        except Exception as e:
            print(e.message)
            print("You may need to install gstreamer1.0-pocketsphinx")
            raise e

        # Process Results From Pipeline With 'self.result()'
        bus = self.pipeline.get_bus()
        bus.add_signal_watch()
        bus.connect('message::element', self.result)

    def listen(self):
        logger.debug("\x1b[32mListening\x1b[0m")
        self.pipeline.set_state(Gst.State.PLAYING)

    def pause(self):
        logger.debug("\x1b[31mPaused\x1b[0m")
        self.pipeline.set_state(Gst.State.PAUSED)

    def result(self, bus, msg):
        msg_struct = msg.get_structure()
        # Ignore Messages That Aren't From Pocketsphinx
        msgtype = msg_struct.get_name()
        if msgtype != 'pocketsphinx':
            return

        # If We Have A Final Command, Send It For Processing
        command = msg_struct.get_string('hypothesis')
        if command != '' and msg_struct.get_boolean('final')[1]:
            logger.debug("Heard: {}".format(command))
            self.emit("finished", command)
