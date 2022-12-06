from pywinauto import application
from pywinauto import timings
import time
import os

app = application.Application()
app.start("C:/KiwoomFlash3/bin/nkministarter.exe")
# 번개 api 불러오기 및 타이틀 이름
title = "번개3 Login"
#로그인 대화 상자를 dlg로 바인딩 dlg로부터 비밀번호/ 비밀번호 입력하는 사용되는
#컨트롤을 구함
dlg = timings.WaitUntilPasses(20, 0.5, lambda: app.window_(title=title))

# pywinauto 패키지를 이용하여 마우스 키보드입력을
#자동화 함
pass_ctrl = dlg.Edit2
pass_ctrl.SetFocus()
pass_ctrl.TypeKeys('xxxx')# 여기지우고 로그인 비밀번호 입력

cert_ctrl = dlg.Edit3
cert_ctrl.SetFocus()
cert_ctrl.TypeKeys('yyyy') # 여기지우고  인증 비밀번호 입력

btn_ctrl = dlg.Button0
btn_ctrl.Click()

time.sleep(50)
os.system("taskkill /im nkmini.exe")

