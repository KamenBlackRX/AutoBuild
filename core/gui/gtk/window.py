import os
import gi
from gi.repository import Gtk


class Window(Gtk.Window):

    def __init__(self, *args, **kwargs):
        gi.require_version('Gtk', '3.0')
        self.windowName = kwargs['name']
        self.defaultButtons = kwargs['defaultButtons']
        self.insanceName = gi.Window

    def createMainWindow(defaultButtons = True):
        pass;