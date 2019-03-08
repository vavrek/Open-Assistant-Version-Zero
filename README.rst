Open Assistant
=============

Open Assistant is a prototype open source voice assistant able 
to interact in basic conversations and automate operating system tasks.

Maintained by the `Open Assistant <http://www.openassistant.org/>`__ 
working group lead by `Andrew Vavrek <https://vavrek.com>`__, this software 
is an extension of `Blather <https://gitlab.com/jezra/blather>`__ 
by `Jezra <http://www.jezra.net/>`__, `Kaylee <https://github.com/Ratfink/kaylee>`__ 
by `Clayton G. Hobbs <https://bzratfink.wordpress.com/>`__, and includes work 
done by `Jonathan Kulp <http://jonathankulp.org/>`__.

This is the first and original version of Open Assistant.
The latest version can be found here:
https://github.com/openassistant/oa-core/tree/next

Dependencies
------------

* `Arch Linux <https://www.archlinux.org/>`_ or `Ubuntu Linux <http://openassistant.org/forum/support/ubuntu-16-04-installation/>`_ (Testing Soon on `macOS <https://www.apple.com/macos>`_)
* `Python 3.5 <https://www.python.org/downloads>`__
* `PocketSphinx 5PreAlpha <https://github.com/cmusphinx/pocketsphinx>`__
* `GStreamer-1.0 <https://github.com/GStreamer/gstreamer>`__
* `GStreamer-1.0 Base Plugins <https://github.com/GStreamer/gst-plugins-base>`__
* `Python-GObject <https://wiki.gnome.org/action/show/Projects/PyGObject>`__
* `Python-Requests <https://pypi.python.org/pypi/requests>`__


Useful Tools
------------

* aplay - console audio player
* plaympeg - console mp3 player
* projectm - visualizations responsive to sound
* wmctrl - window manager control. opening, closing, resize, switch windows. 
* xdotool - command line x automation tool
* xvkbd - virtual keyboard for x

Running Open Assistant
---------------------

* Download and unpack the latest ``openassistant-master.zip`` package.

* Edit ``run.sh`` to configure desired variables, then save.

* Make ``run.sh`` executable with: ``$chmod +x ./run.sh``

* Run ``./run.sh -c -H20 -m0 -M mind/boot``. Global variables will be set and ``run.py`` will launch.

* If ``$MINDDIR/conf/commands.json`` has changed and your machine is online, a new dictionary and language model will be created via the `Sphinx Knowledge Base Tool <http://www.speech.cs.cmu.edu/tools/lmtool.html>`__.

* Say `Launch Open Assistant` to enable operating system control commands such as `Maximize Window` and `Fullscreen`. Say `Launch Stella` to initiate a dialogue with her mind. To have Stella quit say `Goodbye Stella`. Say `Close Open Assistant` to quit operating system command recognition.

* To change assistant commands and language, edit ``conf/commands.json``. Exit and relaunch ``run.sh``.


Open Assistant Versions
=======================

Latest Open Assistant:
https://github.com/openassistant/oa-core/tree/next

Open Assistant fork for Crux System:
https://github.com/s1lvino/c9-ports/tree/master/openassistant
