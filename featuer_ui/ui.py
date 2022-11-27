import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Kiwoom import *
from PyQt5 import uic

form_class = uic.loadUiType("main_window.ui")[0]


class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
         #임포트 키움에서 키움 클래스 인스턴스 생성
        self.Kiwoom = Kiwoom()
        self.Kiwoom.comm_connect()

    def timeout(self):
        current_time =QTime.currentTime()
        text_time = current_time("hh:mm:ss")
        time_msg =" 현재시간:"+ text_time

        state = self.kiwoom.GetConnectState()
        if state ==1:
            state_msg ="서버 연결 중"
        else:
            state_msg = "서버 미 연결중"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
