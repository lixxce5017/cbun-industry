import sys
from datetime import time

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from Kiwoom import *

form_class = uic.loadUiType("main_window.ui")[0]


class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.trade_Stock_done =False

        self.kiwoom = Kiwoom()
        self.kiwoom.comm_connect()

        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.timeout)

        self.lineEdit_first.textChanged.connect(self.code_changed)
        self.pushButton.clicked.connect(self.send_order)

        accouns_num = int(self.kiwoom.get_login_info(("ACCOUNT_CNT")))
        accounts = self.kiwoom.get_login_info("ACCNO")

        accounts_list = accounts.split(';')[0:accouns_num]
        self.comboBox_account.addItems(accounts_list)

        self.lineEdit_first.textChanged.connect(self.code_changed)

        self.load_buy_sell_list()



    def timeout(self):
        # 오픈시간 추가
        market_star_time =QTime(9,0,0)

        current_time = QTime.currentTime()
        # 개장 시간 현재 시간 검사
        if current_time > market_star_time and self.trade_Stock_done is False:
            self.trade_Stocks()
            self.trade_Stock_done =True
        text_time = current_time.toString("hh:mm:ss")
        time_msg = "현재시간 : " + text_time

        state = self.kiwoom.get_connect_state()
        if state == 1:
            state_msg = "서버 접속 중..."
        else:
            state_msg = "서버 미 접속 중..."

        self.statusbar.showMessage(state_msg + " | " + time_msg)

    def code_changed(self):
        code = self.lineEdit_first.text()
        name = self.kiwoom.get_master_code_name(code)
        self.lineEdit_second.setText(name)

    def code_changed(self):
        code = self.lineEdit_first.text()
        name = self.kiwoom.get_master_code_name(code)
        self.lineEdit_second.setText(name)
    def send_order(self):
        order_type_lookup = {'신규매수': 1, '신규매도': 2, '매수취소': 3, '매도취소': 4}
        hoga_lookup = {'지정가': "00", '시장가': "03"}

        account = self.comboBox_account.currentText()
        order_type = self.comboBox_2.currentText()
        code = self.lineEdit_first.text()
        hoga = self.comboBox_3.currentText()
        num = self.spinBox.value()
        price = self.spinBox_2.value()

        self.kiwoom.send_order("send_order_req", "0101", account, order_type_lookup[order_type], code, num, price, hoga_lookup[hoga], "")

        def load_buy_sell_list(self):
            f = open("buy_list.txt", 'rt')
            buy_list = f.readlines()
            f.close()

            f = open("sell_list.txt", 'rt')
            sell_list = f.readlines()
            f.close()

            #buy list와 셀리스트를 읽어오는 메소드

            row_count = len(buy_list) + len(sell_list)
            self.tableWidget_4.setRowCount(row_count)
            # 칼럼에 추가되는 데이터 중 종목명을 구함
            #   바이 리스트
            for j in range(len(buy_list)):
                row_data = buy_list[j]
                split_row_data = row_data.split(';')
                split_row_data[1] = self.kiwoom.get_master_code_name(split_row_data[1].rsplit())

                for i in range(len(split_row_data)):
                    item = QTableWidgetItem(split_row_data[i].rstrip())
                    item.setTextAlignment(Qt.AlignVCenter | Qt.AlignCenter)
                    self.tableWidget_4.setItem(j, i, item)

            # 매도 종목우ㅏ 셀리스트의 종목명과종목 코드를 구함
            for j in range(len(sell_list)):
                row_data = sell_list[j]
                split_row_data = row_data.split(';')
                split_row_data[1] = self.kiwoom.get_master_code_name(split_row_data[1].rstrip())

                for i in range(len(split_row_data)):
                    item = QTableWidgetItem(split_row_data[i].rstrip())
                    item.setTextAlignment(Qt.AlignVCenter | Qt.AlignCenter)
                    self.tableWidget_4.setItem(len(buy_list) + j, i, item)

            self.tableWidget_4.resizeRowsToContents()

            #생선된 파일의 매도 매수 정보를 읽어오는 메소드
        def trade_stocks(self):
            hoga_lookup = {'지정가': "00", '시장가': "03"}

            f = open("buy_list.txt", 'rt')
            buy_list = f.readlines()
            f.close()

            f = open("sell_list.txt", 'rt')
            sell_list = f.readlines()
            f.close()

            # 계정
            account = self.comboBox_account.currentText()

            #BUY 리스트의 데이터를 문자열을 분리하여 필요한 정보를 준비
            for row_data in buy_list:
                split_row_data = row_data.split(';')
                hoga = split_row_data[2]
                code = split_row_data[1]
                num = split_row_data[3]
                price = split_row_data[4]

                #준비된 데이터로 샌드오더
                if split_row_data[-1].rstrip() == '매수전':
                    self.kiwoom.send_order("send_order_req", "0101", account, 1, code, num, price, hoga_lookup[hoga],
                                           "")


            #셀리스트 부분 위와 동일
            # sell list
            for row_data in sell_list:
                split_row_data = row_data.split(';')
                hoga = split_row_data[2]
                code = split_row_data[1]
                num = split_row_data[3]
                price = split_row_data[4]

                if split_row_data[-1].rstrip() == '매도전':
                    self.kiwoom.send_order("send_order_req", "0101", account, 2, code, num, price, hoga_lookup[hoga],
                                           "")
            for i, row_data in enumerate(buy_list):
                buy_list[i] = buy_list[i].replace("매수전", "주문완료")

                # file update
            f = open("buy_list.txt", 'wt')
            for row_data in buy_list:
                f.write(row_data)
            f.close()

            # sell list
            for i, row_data in enumerate(sell_list):
                sell_list[i] = sell_list[i].replace("매도전", "주문완료")

            # file update
            f = open("sell_list.txt", 'wt')
            for row_data in sell_list:
                f.write(row_data)
            f.close()
        # 잔고 체크 메소드
    def check_balance(self):
        self.kiwoom.reset_opw00018_output()
        account_number = self.kiwoom.get_login_info("ACCNO")
        account_number = account_number.split(';')[0]

        self.kiwoom.set_input_value("계좌번호", account_number)
        self.kiwoom.comm_rq_data("opw00018_req", "opw00018", 0, "2000")
        # 보유 종목 데이터 연속 요청
        while self.kiwoom.remained_data:
            time.sleep(0.2)
            self.kiwoom.set_input_value("계좌번호", account_number)
            self.kiwoom.comm_rq_data("opw00018_req", "opw00018", 2, "2000")
        #예수금 데이터를 얻기 위한 opw tr 요청 코드

         # opw00001
        self.kiwoom.set_input_value("계좌번호", account_number)
        self.kiwoom.comm_rq_data("opw00001_req", "opw00001", 0, "2000")

        # balance
        item = QTableWidgetItem(self.kiwoom.d2_deposit)
        item.setTextAlignment(Qt.AlignVCenter | Qt.AlignRight)
        self.tableWidget.setItem(0, 0, item)
            #총매입 평가 손익 수익률 추정자산을
            #Qtabekwidge의 칼럼에 추가 하는 반복문
        for i in range(1, 6):
            item = QTableWidgetItem(self.kiwoom.opw00018_output['single'][i - 1])
            item.setTextAlignment(Qt.AlignVCenter | Qt.AlignRight)
            self.tableWidget.setItem(0, i, item)
        #사이즈 재 조절
        self.tableWidget.resizeRowsToContents()
        #아이템 리스트행과 열 정하기
        item_count = len(self.kiwoom.opw00018_output['multi'])
        self.tableWidget_2.setRowCount(item_count)
        #정한 행과 열의 개수로 아이템 추가 한 종목에 대한 평가손익 수익률 종목명 보유량은 한 행에
        for j in range(item_count):
            row = self.kiwoom.opw00018_output['multi'][j]
            for i in range(len(row)):
                item = QTableWidgetItem(row[i])
                item.setTextAlignment(Qt.AlignVCenter | Qt.AlignRight)
                self.tableWidget_2.setItem(j, i, item)
        #행의 크기를 조절
        self.tableWidget_2.resizeRowsToContents()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()

