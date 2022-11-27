import sys
from PyQt5.QtWidgets import *
import Kiwoom
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




if __name__ == "__main__":
    app = QApplication(sys.argv)
    pymon = PyMon()
    pymon.run()