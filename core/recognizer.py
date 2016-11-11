# OpenAssistant 0.04
# 2016 General Public License V3
# By Andrew Vavrek, Clayton G. Hobbs, Jezra, Jonathan Kulp

# recognizer.py - Voice Recognition

import os.path
import sys

import gi
gi.require_version('Gst', '1.0')
from gi.repository import GObject, Gst
GObject.threads_init()
Gst.init(None)


class Recognizer(GObject.GObject):
    __gsignals__ = {
        'finished' : (GObject.SIGNAL_RUN_LAST, GObject.TYPE_NONE,
                      (GObject.TYPE_STRING,))
    }

    def __init__(self, config):
        GObject.GObject.__init__(self)
        self.commands = {}

        # Configure Audio Source
        src = config.options['microphone']
        if src:
            audio_src = 'alsasrc device="hw:{0},0"'.format(src)
        else:
            audio_src = 'autoaudiosrc'

        # Build Pipeline
        cmd = (
            audio_src +
            ' ! audioconvert' +
            ' ! audioresample' +
            ' ! pocketsphinx lm=' + config.lang_file + ' dict=' +
            config.dic_file +
            ' ! appsink sync=false'
        )
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
