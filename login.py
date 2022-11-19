from pywinauto import application
from pywinauto import timings
import time
import os

app = application()
app.start("C/:KiwoomFlash3/bin/nkministarter.exe")

title = "번개 로그인"
dlg= timings.WaitUntilPasses(20,0,5,lambda :app.window_(title=title))

