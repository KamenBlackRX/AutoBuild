import os
import gi


class Window(Gtk.Window):

    from gi.repository import Gtk
    gi.require_version('Gtk', '3.0')

    def __init__(self, *args, **kwargs):
        self.windowName = kwargs['name']
        self.defaultButtons = kwargs['defaultButtons']
