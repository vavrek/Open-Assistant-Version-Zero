# OpenAssistant 0.01
# 2016 General Public License V3
# By Andrew Vavrek, Clayton G. Hobbs, Jezra

# gui.py - Graphical Assistant Control (Buggy)

import sys
import gi
from gi.repository import GObject

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk


class GTKTrayInterface(GObject.GObject):
    __gsignals__ = {
        'command' : (GObject.SIGNAL_RUN_LAST, GObject.TYPE_NONE,
                     (GObject.TYPE_STRING,))
    }
    idle_text = "OpenAssistant: Paused"
    listening_text = "OpenAssistant: Listening"

    def __init__(self, args, continuous):
        GObject.GObject.__init__(self)
        self.continuous = continuous

        self.statusicon = Gtk.StatusIcon()
        self.statusicon.set_title("OpenAssistant")
        self.statusicon.set_name("OpenAssistant")
        self.statusicon.set_tooltip_text(self.idle_text)
        self.statusicon.set_has_tooltip(True)
        self.statusicon.connect("activate", self.continuous_toggle)
        self.statusicon.connect("popup-menu", self.popup_menu)

        self.menu = Gtk.Menu()
        self.menu_listen = Gtk.MenuItem('Listen')
        self.menu_continuous = Gtk.CheckMenuItem('Continuous')
        self.menu_quit = Gtk.MenuItem('Quit')
        self.menu.append(self.menu_listen)
        self.menu.append(self.menu_continuous)
        self.menu.append(self.menu_quit)
        self.menu_listen.connect("activate", self.toggle_listen)
        self.menu_continuous.connect("toggled", self.toggle_continuous)
        self.menu_quit.connect("activate", self.quit)
        self.menu.show_all()

    def continuous_toggle(self, item):
        checked = self.menu_continuous.get_active()
        self.menu_continuous.set_active(not checked)

    def toggle_continuous(self, item):
        checked = self.menu_continuous.get_active()
        self.menu_listen.set_sensitive(not checked)
        if checked:
            self.menu_listen.set_label("Listen")
            self.emit('command', "continuous_listen")
            self.statusicon.set_tooltip_text(self.listening_text)
            self.set_icon_active()
        else:
            self.set_icon_inactive()
            self.statusicon.set_tooltip_text(self.idle_text)
            self.emit('command', "continuous_stop")

    def toggle_listen(self, item):
        val = self.menu_listen.get_label()
        if val == "Listen":
            self.set_icon_active()
            self.emit("command", "listen")
            self.menu_listen.set_label("Stop")
            self.statusicon.set_tooltip_text(self.listening_text)
        else:
            self.set_icon_inactive()
            self.menu_listen.set_label("Listen")
            self.emit("command", "stop")
            self.statusicon.set_tooltip_text(self.idle_text)

    def popup_menu(self, item, button, time):
        self.menu.popup(None, None, Gtk.StatusIcon.position_menu, item, button, time)

    def run(self):
        # SET THE ICON
        self.set_icon_inactive()
        if self.continuous:
            self.menu_continuous.set_active(True)
            self.set_icon_active()
        else:
            self.menu_continuous.set_active(False)
        self.statusicon.set_visible(True)

    def quit(self, item):
        self.statusicon.set_visible(False)
        self.emit("command", "quit")

    def finished(self, text):
        if not self.menu_continuous.get_active():
            self.menu_listen.set_label("Listen")
            self.set_icon_inactive()
            self.statusicon.set_tooltip_text(self.idle_text)

    def set_icon_active_asset(self, i):
        self.icon_active = i

    def set_icon_inactive_asset(self, i):
        self.icon_inactive = i

    def set_icon_active(self):
        self.statusicon.set_from_file(self.icon_active)

    def set_icon_inactive(self):
        self.statusicon.set_from_file(self.icon_inactive)


class GTKInterface(GObject.GObject):
    __gsignals__ = {
        'command': (GObject.SIGNAL_RUN_LAST, GObject.TYPE_NONE,
                    (GObject.TYPE_STRING,))
    }

    def __init__(self, args, continuous):
        GObject.GObject.__init__(self)
        self.continuous = continuous

        # MAKE A WINDOW
        self.window = Gtk.Window(Gtk.WindowType.TOPLEVEL)
        self.window.connect("delete_event", self.delete_event)

        # GIVE THE WINDOW A NAME
        self.window.set_title("OpenAssistant")
        self.window.set_resizable(False)

        layout = Gtk.VBox()
        self.window.add(layout)

        # MAKE A LISTEN/STOP BUTTON
        self.lsbutton = Gtk.Button("Listen")
        layout.add(self.lsbutton)

        # MAKE A CONTINUOUS BUTTON
        self.ccheckbox = Gtk.CheckButton("Continuous Listen")
        layout.add(self.ccheckbox)

        # CONNECT THE BUTTONS
        self.lsbutton.connect("clicked", self.lsbutton_clicked)
        self.ccheckbox.connect("clicked", self.ccheckbox_clicked)

        # ADD A LABEL TO THE UI TO DISPLAY THE LAST COMMAND
        self.label = Gtk.Label()
        layout.add(self.label)

        # CREATE AN ACCELLERATOR GROUP FOR THIS WINDOW
        accel = Gtk.AccelGroup()

        # ADD THE CTRL+Q TO QUIT
        accel.connect(Gdk.keyval_from_name('q'), Gdk.ModifierType.CONTROL_MASK,
                Gtk.AccelFlags.VISIBLE, self.accel_quit)

        # LOCK THE GROUP
        accel.lock()
        
        # ADD THE GROUP TO THE WINDOW
        self.window.add_accel_group(accel)

    def ccheckbox_clicked(self, widget):
        checked = self.ccheckbox.get_active()
        self.lsbutton.set_sensitive(not checked)
        if checked:
            self.lsbutton_stopped()
            self.emit('command', "continuous_listen")
            self.set_icon_active()
        else:
            self.emit('command', "continuous_stop")
            self.set_icon_inactive()

    def lsbutton_stopped(self):
        self.lsbutton.set_label("Listen")

    def lsbutton_clicked(self, button):
        val = self.lsbutton.get_label()
        if val == "Listen":
            self.emit("command", "listen")
            self.lsbutton.set_label("Stop")
            # CLEAR LABEL
            self.label.set_text("")
            self.set_icon_active()
        else:
            self.lsbutton_stopped()
            self.emit("command", "stop")
            self.set_icon_inactive()

    def run(self):
        # SET DEFAULT ICON
        self.set_icon_inactive()
        self.window.show_all()
        if self.continuous:
            self.set_icon_active()
            self.ccheckbox.set_active(True)

    def accel_quit(self, accel_group, acceleratable, keyval, modifier):
        self.emit("command", "quit")

    def delete_event(self, x, y):
        self.emit("command", "quit")

    def finished(self, text):
        # IF CONTINUOUS IS NOT SELECTED
        if not self.ccheckbox.get_active():
            self.lsbutton_stopped()
            self.set_icon_inactive()
        self.label.set_text(text)

    def set_icon_active_asset(self, i):
        self.icon_active = i

    def set_icon_inactive_asset(self, i):
        self.icon_inactive = i

    def set_icon_active(self):
        Gtk.Window.set_default_icon_from_file(self.icon_active)

    def set_icon_inactive(self):
        Gtk.Window.set_default_icon_from_file(self.icon_inactive)
