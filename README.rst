Open Assistant (Version Zero)
=============

Open Assistant is a prototype open source voice assistant able to automate operating system tasks and engage in simple scripted conversations.

This is "Version Zero" of Open Assistant, which is highly Linux dependent.

`The newest version of OA Core<https://github.com/openassistant/oa-core>`_ runs entirely in Python and is more portable.

Check out what `kidsodateless <https://github.com/kidsodateless/oa-core>`_ did with it: `https://youtu.be/D99V9Ge9IaE <https://youtu.be/D99V9Ge9IaE>`


Dependencies
------------

* `Arch Linux <https://www.archlinux.org/>`_ or `Ubuntu Linux <http://openassistant.org/forum/support/ubuntu-16-04-installation/>`_
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

*  `Download <https://github.com/vavrek/Open-Assistant/archive/master.zip>`__ and extract the latest ``Open-Assistant-master.zip`` package.

* Edit ``oa.sh`` to choose your desired variables, then save.

* Make ``oa.sh`` executable with: ``$chmod +x ./oa.sh``

* Launch ``./oa.sh``

* Command variables will be set and ``oa.py`` will run.

* If ``$MINDDIR/words/commands.json`` has been changed and your machine is online, a new dictionary and language model will be created via the `Sphinx Knowledge Base Tool <http://www.speech.cs.cmu.edu/tools/lmtool.html>`__.

* Say "Hello Stella" and listen for a reply. You will need to adjust your microphone settings and avoid noisy environments for best results.

* To learn and change commands, edit ``words/commands.json``. Save, quit ``oa.py``, then relaunch ``oa.sh`` to update.


Learn More
=======================
OA Main Site: https://openassistant.org/wp/

OA Wiki: https://github.com/openassistant/oa-core/wiki

Maintained by working group lead by `Andrew Vavrek <https://vavrek.com>`__, Open Assistant 
is an extension of `Blather <https://gitlab.com/jezra/blather>`__ 
by `Jezra <http://www.jezra.net/>`__, `Kaylee <https://github.com/Ratfink/kaylee>`__ 
by `Clayton G. Hobbs <https://bzratfink.wordpress.com/>`__, and includes work 
done by `Jonathan Kulp <http://jonathankulp.org/>`__.

Support OA!
=======================
Patreon: https://www.patreon.com/openassistant
