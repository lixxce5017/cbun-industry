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
        self.set_signal_slots()
    def _create_kiwoom_instance(self):
        self.setControl("KHOPENAPI.KHOpenAPICtrl.1")

    def _set_signal_slots(self):
        self.OnEventConnect.connect(self._event_connect)
        self.OnReceiveTrData.connect(self._receive_tr_data)

    def comm_connect(self): #키움 객체가 생성이 되면 커넥트 메서드 호출 로그인 실행
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

    def get_master_code_name(self, code):
        code_name = self.dynamicCall("GETMASTERCODENAME(QString",code)

    def get_connect_state(self):
        ret =self.dynamicCall("GetConnectState()")
        return ret
    def set_input_value(self, id,value):
        self.dynamicCall("SetInputValue(QString,QString)", id,value)

    def comm_rq_data(self,rqname,trcode,next,screen_no):
        self.dynamicCall("COmmRqData(QString,QString,int,QString) ",rqname,trcode,next,
                         screen_no)
        self.tr_event_loop =QEventLoop()
        self.tr_event_loop.exec_()


        #코드 타입 이름 인덱스 아이템 이름까지 모두 다이나믹콜 후 ret 반환
    def comm_get_data(self,code,real_type,field_name,index,item_name):
        ret =self.dynamicCall("CommGetData(QString, Qstring,QString,int QString)",
                              code,real_type, field_name,item_name)
        return ret.strip()

    def _get_repat_cnt(self,trcode,rqname):
        ret = self.dynamicCall("GetRepeatCnt(QString,Qstring)", trcode,rqname)
        return ret