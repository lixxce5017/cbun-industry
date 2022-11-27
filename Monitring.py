import sys
from PyQt5.QtWidgets import *
import Kiwoom
import time
from pandas import DataFrame
import datetime

MARKET_KOSPI =0
MARKET_KISDAQ=0

class PyMon:
    def __init__(self):
        self.kiwoom = Kiwoom.Kiwoom()
        self.kiwoom.comm_connect()

    def run(self):
        print("실행")

    #유가 증권시장 코스닥 가져옴
    def get_code_list(self):
        self.kospi_codes = self.kiwoom.get_code_list_by_market(MARKET_KOSPI)
        self.kosdaq_codes = self.kiwoom.get_code_list_by_market(MARKET_KISDAQ)


        #일 별 데이터 가져오기
        # 인자로 종목 코드와 기준일자 받음
    def get_ohlcv(self, code, start):
        self.kiwoom.ohlcv = {'date': [], 'open': [], 'high': [], 'low': [], 'close': [], 'volume': []}

        self.kiwoom.set_input_value("종목코드", code)
        self.kiwoom.set_input_value("기준일자", start)
        self.kiwoom.set_input_value("수정주가구분", 1)
        self.kiwoom.comm_rq_data("opt10081_req", "opt10081", 0, "0101")
        time.sleep(0.2)

        df = DataFrame(self.kiwoom.ohlcv, columns=['open', 'high', 'low', 'close', 'volume'],
                       index=self.kiwoom.ohlcv['date'])
        return df

    #되는지 본느거
    def run(self):
        df = self.get_ohlcv(sys.argv)
        pymon =PyMon()
        pymon.run()

    #급등주 포착
    def chek_seepdy_rising_volume(self, code):
        today =datetime.datetime.today().strftime("%y%m%d") #오늘 날짜부터 가져옴
        df = self.get_ohlcv(code,today) #get ohlcv 메서드를 호출해서 해당 종목 정보를 datframe 객체로 얻어오고 바인딩
        volumes = df['volume']


if __name__ == "__main__":
    app = QApplication(sys.argv)
    pymon = PyMon()
    pymon.run()