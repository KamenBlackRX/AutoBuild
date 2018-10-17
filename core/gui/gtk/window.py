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

class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Autobuild")
        # add a box to hold all
        self.hbox = Gtk.Box()

        self.button = Gtk.Button(label="Start Autobuild")
        self.button.connect("clicked", self.on_button_clicked)
   

        #Add Label
        self.label = Gtk.Label()
        self.label.set_label = "The Auto Build program for Fast Enviroment Configuration"
        self.add(self.hbox)

    def on_button_clicked(self, widget):
        print("Started Autobuild")