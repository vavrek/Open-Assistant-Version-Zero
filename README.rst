OpenAssistant
=============

OpenAssistant is an evolving open source artificial intelligence system able 
to interact in basic conversation and automate an increasing number of tasks.

Maintained by the `OpenAssistant <http://www.openassistant.org/>`__ 
working group lead by `Andrew Vavrek <http://www.vavrek.com/>`__, this software 
is an extension of `Blather <https://gitlab.com/jezra/blather>`__ 
by `Jezra <http://www.jezra.net/>`__, `Kaylee <https://github.com/Ratfink/kaylee>`__ 
by `Clayton G. Hobbs <https://bzratfink.wordpress.com/>`__, and includes work 
done by `Jonathan Kulp <http://jonathankulp.org/>`__.


Dependencies
------------

* `Arch <https://www.archlinux.org/>`_ or `Ubuntu Linux <http://openassistant.org/forum/support/ubuntu-16-04-installation/>`_ (Testing Soon on `macOS <https://www.apple.com/macos>`_)
* `Python 3.5 <https://www.python.org/downloads>`__
* `PocketSphinx 5PreAlpha <https://github.com/cmusphinx/pocketsphinx>`__
* `GStreamer-1.0 <https://github.com/GStreamer/gstreamer>`__
* `GStreamer-1.0 Base Plugins <https://github.com/GStreamer/gst-plugins-base>`__
* `Python-GObject <https://wiki.gnome.org/action/show/Projects/PyGObject>`__
* `Python-Requests <https://pypi.python.org/pypi/requests>`__


Useful Tools
------------

* aplay - console audio player
* pamixer - portaudio volume control
* plaympeg - console mp3 player
* projectm - visualizations responsive to sound
* wmctrl - window manager control. opening, closing, resize, switch windows. 
* xdotool - command line x automation tool
* xvkbd - virtual keyboard for x

Running OpenAssistant
---------------------

* Install dependencies and tools.

* Download and unpack the latest ``openassistant-master.zip`` package.

* Edit ``assist.sh`` to configure desired variables, then save.

* Make ``assist.sh`` executable with: ``$chmod +x ./assist.sh``

* Run ``./assist.sh``. Global variables will be set and ``assistant.py`` will launch.

* If ``./etc/commands.json`` has changed and your machine is online, a new dictionary and language model will be created via the `Sphinx Knowledge Base Tool <http://www.speech.cs.cmu.edu/tools/lmtool.html>`__.

* Say "Hello!" :) To mute, say "Be quiet" or "Silence". To unmute, say "Talk to me". 

* To quit, say "Goodbye" or "Farewell."

* To change assistant commands and language, edit ``./etc/commands.json``. Exit and relaunch ``assist.sh``.

* For help, you can receive support in the `OpenAssistant Forum <http://openassistant.org/community/>`_.


Next Steps
----------

* Port OpenAssistant to multiple Linux distributions, beginning with Ubuntu

* Enable dynamic voice and instant name changes via spoken commands

* Configure syntax and actions via spoken commands

* Install internal language model translation

* Improve speech recognition and synthesis

* Long-term memory & machine learning

* Web scraping & information analysis

* Establish multiple default 'personalities' and plug-in functions

* Port OpenAssistant to all operating systems and devices

* Galactic Exploration!


Join Us!
--------

Join our development working group at: http://www.openassistant.org
