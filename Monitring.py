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

        if(len(volumes))< 21: #20일치의 데이터만 쓰니 21이면 ㄴㄴ
            return False
        sum_vol20 = 0 # 일 별거래량 누적
        today_vol = 0

        for i, vol in enumerate(volumes):
            if i==0:
                today_vol =vol
            elif 1<=i <=20:
                sum_vol20 += vol
            else:   # 여기도 쓸데 없이 더 안돌리고 20일 필요하니 브레이크 탈출
                break
        avg_vol20 = sum_vol20/20    # 평균 20일의 거래량 계산 후 시작 거래일의 거래량과 비교
                                    # 거래량이 평균 거래량 1,000% 초과시 true 리턴
        if today_vol > avg_vol20 * 10:
            return True
    # 선정된 종목 정보파일로 쓰기
    def update_buy_list(self, buy_list):
        f= open("buy_list.txt", "wt")
        for code in buy_list:
            f.writelines("매수;%s; 시장가;10;0;매수전\n" %(code))
        f.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    pymon = PyMon()
    pymon.run()