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

    def __init__(self, config):
        GObject.GObject.__init__(self)
        self.commands = {}
        logger.debug("Initializing Recognizer")
        logger.debug(config)
        logger.debug(config.options)

        # Configure Audio Source
        src = config.options['microphone']
        if src:
            #audio_src = 'alsasrc device="hw:{0},0"'.format(src)
            audio_src = 'autoaudiosrc device="hw:{0},0"'.format(src)
        else:
            audio_src = 'autoaudiosrc'

        # Build Pipeline
        cmd = (
            audio_src +
            ' ! audioconvert' +
            ' ! audioresample' +
            ' ! pocketsphinx {}'.format(' '.join([
                    '{}={}'.format(opt, val) for opt, val in [
                        ('lm', config.lang_file), 
                        ('dict', config.dic_file),
                        ('fsg', config.fsg_file)
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
        self.pipeline.set_state(Gst.State.PLAYING)

    def pause(self):
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
            self.emit("finished", command)