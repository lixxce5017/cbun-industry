from datetime import date

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
        self.OnReceiveChejanData.connect(self._recive_chejan_data)

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
    def _comm_get_data(self,code,real_type,field_name,index,item_name):
        ret =self.dynamicCall("CommGetData(QString, Qstring,QString,int QString)",
                              code,real_type, field_name,item_name)
        return ret.strip()

    def _get_repat_cnt(self,trcode,rqname):
        ret = self.dynamicCall("GetRepeatCnt(QString,Qstring)", trcode,rqname)
        return ret
    #데이터 받기 이벤트 부분
    def _receive_tr_data(self, screen_no, rqname, trcode, recode_name,next,unused1, unused2
                         ,unused3,unused4):

        if next =='2':
            self.remained_data = True

        else:
            self.remained_data= False

        if rqname == "opt10081_req":
            self._opt10081(rqname, trcode)
        elif rqname == "opw00001_req":
            self._opw00001(rqname, trcode)
        elif rqname == "opw00018_req":
            self._opw00018(rqname, trcode)

        try:
            self.tr_event_loop.exit()

        except AttributeError:
            pass

    def _opt10081(self, rqname,trcode):
        data_cnt = self._get_repeat_cnt(trcode, rqname)
        #tr코드 rqname 일자 모두 cnt 수만큼 데이터에 집어 넣어줌
        for i in range(data_cnt):
            data = self._comm_get_data(trcode,"", rqname,i,"일자")
            open = self.comm_get_data(trcode,"",rqname,i,"시가")
            high =self.comm_get_data(trcode,"",rqname,"고가")
            low =self.comm_get_data(trcode,"", rqname,i, "저가")
            close = self.comm_get_data(trcode,"",rqname,i,"현재가")
            volume = self.comm_get_data(trcode, "",rqname,i,"거래량")

            self.ohlcv['date'].append(date)
            self.ohlcv['open'].append(int(open))
            self.ohlcv['high'].append(int(high))
            self.ohlcv['low'].append(int(low))
            self.ohlcv['close'].append(int(close))
            self.ohlcv['volume'].append(int(volume))


   #주문 보내기 다이나믹콜
    def send_oder(self,rqname,screen_no, acc_no,order_type,code,quantity,
                  price,hoga,order_no):
        self.dynamicCall("SendOrder(Qstring,Qstirng,int,Qstring,int,int,Qstring,Qstring)",
                         [rqname,screen_no,acc_no,order_type,code,quantity,price,hoga,order_no])



    def get_hchejan_data(self,fid):# 체결잔고 데이터를 가져오는 메서드
        ret = self.dynamicCall("GetChejanData(int)", fid)
        return ret

        #서로다른 fid 값으로 서로 다른 데이터를 가져옴
        #9023 주문번호 900 주문수량 901 주문가격
    def _recive_chejan_data (self,gubun,item_cnt,fid_list):
        print(gubun)
        print(self.get_chejan_data(9203))
        print(self.get_chejan_data(302))
        print(self.get_chejan_data(900))
        print(self.get_chejan_data(901))

    def get_login_info(self,tag):
        ret = self.dynamicCall("GetLoginInfo(Qstring)", tag)
        return ret

    #TR을 사용하기 위한 메소드
    def _opw00001(self,rqname,trcode):

        d2_deposit = self._comm_get_data(trcode,"",rqname,0,"d+추정 예수금")
        self.deposit =Kiwoom.change_format(d2_deposit)
        if rqname =="opt10081_req":
            self.opt10081(rqname,trcode)

        elif rqname =="opw00001_req":
            self._opw00001(rqname,trcode)


    def change_format(data):
        strip_data = data.lstrip('-0')
        if strip_data =='' or strip_data =='.00':
            strip_data ='0'

        format_data =format(int(strip_data),',d')
        if data.startswith('-'):
            format_data = '-' + format_data

        return format_data

    #수익률에 대한 포맷 변경
    def change_format2(data):
        strip_data = data.lstrip('-0')

        if strip_data == '':
            strip_data = '0'

        if strip_data.startswith('.'):
            strip_data = '0' + strip_data

        if data.startswith('-'):
            strip_data = '-' + strip_data

        return strip_data

    #tr코드 추가 싱글 데이터로 잔고 데이터
    #reapt_cnt 메소드 호출하여 보유종 목을 받아옴
    # 그 후 해당 개수만큼 반복하여 종목 상세 데이터를
    #get data로 받아옴
    def _opw00018(self, rqname, trcode):
        total_purchase_price = self.comm_get_data(trcode,"",rqname ,0,"총매입금액")
        total_eval_price =self.comm_get_data(trcode,"",rqname,"총평가금액")
        total_earning_rate = self.comm_get_data(trcode,"",rqname,0,"총수익률(%)")
        estimated_deposit = self.comm_get_data(trcode,"",rqname,0,"추정예탁자산 ")
        total_eval_profit_loss_price = self._comm_get_data(trcode,"",rqname,0,"총평가손익금액")

        #세부 ㅇㅇ데이터 변환
        self.opw00018_output['single'].append(Kiwoom.change_format(total_purchase_price))
        self.opw00018_output['single'].append(Kiwoom.change_format(total_eval_price))
        self.opw00018_output['single'].append(Kiwoom.change_format(total_eval_profit_loss_price))

        total_earning_rate = Kiwoom.change_format(total_earning_rate)

        if self.get_server_gubun():
            total_earning_rate = float(total_earning_rate) / 100
            total_earning_rate = str(total_earning_rate)


        self.opw00018_output['single'].append(Kiwoom(total_earning_rate))
        self.opw00018_output['single'].append(Kiwoom.change_format(estimated_deposit))



        rows = self._getrepeat_cnt(trcode,rqname)
        #reapt_cnt 메소드 호출하여 보유종 목을 받아옴
    # 그 후 해당 개수만큼 반복하여 종목 상세 데이터를
    #get data로 받아옴
        for i in range(rows):
            name =self._comm_get_data(trcode,"",rqname,i,"종목명")
            quantity = self._comm_get_data(trcode,"",rqname,i,"보유수량")
            purchase_price =self._comm_get_data(trcode,"",rqname,i,"매입가")
            current_price = self._comm_get_data(trcode,"",rqname,i,"평가손익")
            eval_profit_loss_price = self._comm_get_data(trcode,"",rqname,i,"평가손익")
            earning_rate = self._comm_get_data(trcode,"", rqname,i,"수익률(%)")

            quantity = Kiwoom.change_format(quantity)
            purchase_price = Kiwoom.change_format(purchase_price)
            current_price = Kiwoom.change_format(eval_profit_loss_price)
            earning_rate = Kiwoom.change_format2(earning_rate)
            self.opw00018_output['multi'].append([name, quantity, purchase_price, current_price, eval_profit_loss_price,
                                                  earning_rate])

            #ㅂㄷ아온 데이터를 인서트변수에 리스트에 저장
    def reset_opw00018_output(self):
                self._opw00018_output = {'single': [], 'multi': []}

    #서버 접속을 구분해서 데이터 다르게 처리
    def get_server_gubun(self):
        ret = self.dynamicCall("KOA_Funtions(QString, QString)","GetServerGunbun","")
        return ret

