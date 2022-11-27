import sys
from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import *
from PyQt5.QtCore import *
import time
import pandas as pd
import sqlite3

class Kiwwom(QAxWidget):
    def __init__(self):
        super().__init__()