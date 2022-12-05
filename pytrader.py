import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from kiwoom import *

form_class = uic.loadUiType("main_window.ui")


class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.kiwoom = Kiwoom()
        self.kiwoom.comm_connect()

        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.timeout)

        self.lineEdit.textChanged.connect(self.code_changed)
        self.pushButton.clicked.connect(self.send_order)

        accouns_num = int(self.kiwoom.get_login_info(("ACCOUNT_CNT")))
        accounts = self.kiwoom.get_login_info("ACCNO")

        accounts_list = accounts.split(';')[0:accouns_num]
        self.comboBox.addItems(accounts_list)

        self.lineEdit.textChanged.connect(self.code_changed)

        self.load_buy_sell_list()



    def timeout(self):
        current_time = QTime.currentTime()
        text_time = current_time.toString("hh:mm:ss")
        time_msg = "현재시간 : " + text_time

        state = self.kiwoom.get_connect_state()
        if state == 1:
            state_msg = "서버 접속 중..."
        else:
            state_msg = "서버 미 접속 중..."

        self.statusbar.showMessage(state_msg + " | " + time_msg)

    def code_changed(self):
        code = self.lineEdit.text()
        name = self.kiwoom.get_master_code_name(code)
        self.lineEdit_2.setText(name)

    def code_changed(self):
        code = self.lineEdit.text()
        name = self.kiwoom.get_master_code_name(code)
        self.lineEdit_2.setText(name)
    def send_order(self):
        order_type_lookup = {'신규매수': 1, '신규매도': 2, '매수취소': 3, '매도취소': 4}
        hoga_lookup = {'지정가': "00", '시장가': "03"}

        account = self.comboBox.currentText()
        order_type = self.comboBox_2.currentText()
        code = self.lineEdit.text()
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()

