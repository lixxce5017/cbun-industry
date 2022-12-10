****주식 추천 프로그램****<br/>
**산업스파이**<br/><br/><br/><br/>
  
****사용 방법****<br/><br/>

****의존성****<br/><br/>
pyhon 3.x<br/>
*키움증권 번개 api*<br/>
[키움증권사이트](https://www.kiwoom.com/h/common/event/VEventMainView?eventCode=20220074&from=138<br/>) *계좌개설 필요 *<br/>
키움증권 오픈 api 모듈api*<br/>
Open API OCX 탑재 프로그램 제작 및 KOA Studioapi*<br/>
아나콘다 32bit api*<br/>


<br/><br/>

``` python 

class Kiwoom(QAxWidget): 
    def __init__(self):
        super().__init__()
        self._create_kiwoom_instance()

    def _create_kiwoom_instance(self):
        self.setControl("KHOPENAPI.KHOpenAPICtrl.1")

    def comm_connet(self):
        self.dynamicCall("CommConnect()")
        self.login_event_loop =QEventLoop()
        self.login_event_loop.exec_()

    def _event_connect(self, err_code):
        if err_code ==0:
            print("연결")
        else:
            print("연결안됨")

        self.login_event_loop.exit()

    def get_code_list_by_market(self, market): 
        code_list = self.dynamicCall("getcodlistmarket(QString)", market)
        code_list =code_list.split(';')
        return code_list[:-1]



if __name__=="__main__":
    app = QApplication(sys.argv)
    kiwoom = Kiwoom()
    code_list = kiwoom.get_code_list_by_market('10')
    for code in code_list: 
        print(code, end=" ")


```

```app = application()
app.start("C/:KiwoomFlash3/bin/nkministarter.exe")

title = "번개 로그인"

#로그인 대화 상자를 dlg로 바인딩 dlg로부터 비밀번호/ 비밀번호 입력하는 사용되는
#컨트롤을 구함
dlg= timings.WaitUntilPasses(20,0,5,lambda :app.window_(title=title))


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


```

****설치방법****<br/><br/>
[키움증권 다운로드 사이트](https://www.kiwoom.com/h/customer/download/VOpenApiInfoView?dummyVal=0)<br/>
0. 키움증권 회원가입/계좌개설/공동인증서 로그인<br/>
1.오픈api 신청<br/>
2.open api 모듈 다운로드<br/>
3 번개 api 다운로드<br/>
4.KOA Studio 다운로드<br/>
5. 아나콘다 설치 후 32bit 변경<br/>

[설명해주는 사이트](https://losskatsu.github.io/it-infra/conda32/#4-%ED%82%A4%EC%9B%80-api-%EB%8B%A4%EC%9A%B4%EB%A1%9C%EB%93%9C)<br/>

모두 설치


****Contributer****
