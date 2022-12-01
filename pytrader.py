import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from kiwoom import *

form_class = uic.loadUiType("main_window.ui")

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
