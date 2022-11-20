from PyQt5.QtCore import *
import time
import pandas as pd
import sqlite3
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QAxContainer import *
import sys


TR_REQ_TIME_INTERVAL = 0.2

# 오픈 API를 쉽게 사용할 수 해주는 클래스
class Kiwoom(QAxWidget): # 키움 오픈 API를 이용하려면 QaXWidget 가 필요
    def __init__(self):
        super().__init__()
        self._create_kiwoom_instance()

    def _create_kiwoom_instance(self):
        self.setControl("KHOPENAPI.KHOpenAPICtrl.1")

    def comm_connet(self): #키움 객체가 생성이 되면 커넥트 메서드 호출 로그인 실행
        self.dynamicCall("CommConnect()")
        self.login_event_loop =QEventLoop()
        self.login_event_loop.exec_()

    def _event_connect(self, err_code):
        if err_code ==0:
            print("연결")
        else:
            print("연결안됨")

        self.login_event_loop.exit()

    def get_code_list_by_market(self, market): #get code market 메소드를 동적호출
        code_list = self.dynamicCall("getcodlistmarket(QString)", market)
        code_list =code_list.split(';')
        return code_list[:-1]



if __name__=="__main__":
    app = QApplication(sys.argv)
    kiwoom = Kiwoom()
    code_list = kiwoom.get_code_list_by_market('10')
    for code in code_list: #리턴 받은 종목 코드 리스트 한 줄씩 출력
        print(code, end=" ")
