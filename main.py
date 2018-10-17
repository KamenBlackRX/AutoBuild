#!/usr/bin/python
# -*- coding: utf-8 -*-

# Autobuild

import os
import sys
import PySide2.QtCore
import random
from PySide2 import QtCore, QtWidgets, QtGui, QtUiTools
import threading

class Utils(object):
    def __init__(self):
        pass

    def loadUiForm(self, uiPath):
        loader = QtUiTools.QUiLoader()
        file = QtCore.QFile(uiPath)
        file.open(QtCore.QFile.ReadOnly)
        LoadedWidget = loader.load(file, self)
        file.close()
        return LoadedWidget

class WizardWindow(QtWidgets.QWidget):
    def __init__(self):
        pass

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.counter = 0
        self.hello = [
            "Welcome to AutoBuild System",
            "Bem vindo ao Autobuild System",
            "アウトブイォえうこそ"
        ]

        self.button = QtWidgets.QPushButton("Click here for start!")
        self.text = QtWidgets.QLabel(self.hello[0])
        self.text.setAlignment(QtCore.Qt.AlignCenter)

        self.text.setFont(QtGui.QFont("Titillium", 30))
        self.button.setFont(QtGui.QFont("Titillium", 20))

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

        self.button.clicked.connect(self.startProcess)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.magic)
        timer.start(3000)
                           

    def startProcess(self):
        print('start')

    def magic(self):
        if self.counter >= len(self.hello):
            self.counter = 0
        self.text.setText(self.hello[self.counter])
        self.counter +=1
        
if __name__ == "__main__":
    # Prints PySide version
    # e.g. 1.0.2
    print('PySide2 Version:', PySide2.__version__)

    # Gets a tuple with each version component
    # e.g. (1, 0, 2, 'final', 1)
    print('PySide2 Final Version:',PySide2.__version_info__)

    # Prints the Qt version used to compile PySide
    # e.g. "5.11.0"
    print('PySide2.QtCore Version:',PySide2.QtCore.__version__)

    # Gets a tuple with each version components of Qt used to compile PySide
    # e.g. (5, 11, 0)
    print('PySide2.QtCore Compile Version:',PySide2.QtCore.__version_info__)


    app = QtWidgets.QApplication([])

    widget = MainWindow()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec_())