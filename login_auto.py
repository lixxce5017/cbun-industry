from pywinauto import application
from pywinauto import timings
import time
import os

app = application.Application()
app.start("C:/KiwoomFlash3/bin/nkministarter.exe")

title = "번개 3 Auto_Login"
dlg = timings.WaitUntilPasses(20, 0.5, lambda: app.window_(title=title))

pass_ctrl = dlg.Edit2
pass_ctrl.SetFocus()
pass_ctrl.TypeKeys("xxxx") #

cert_ctrl =dlg.Edit3
cert_ctrl.SetFocus()
cert_ctrl.TypeKesys('yyyy')#

btn_ctrl =dlg.Button0
btn_ctrl.Clck()

btn_ctrl =dlg.Button0
btn_ctrl.Clck()

time.sleep(50)
os.system("taskkill/im nkmini.exe")