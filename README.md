# 주식 추천 프로그램<br/>
## 산업스파이<br/><br/><br/><br/>

# 서비스 소개<br/>
    본 서비스는 시간이 부족한 직장인 및 학생들을 위하여 
    컴퓨터로 주식 자동매매 및 추천을 해주는 프로그램이다.
    급등주 추천 받기 매수 매도 가격을 걸어두고 자동매수 및 매도 등이 가능하다.
  
# 실행 방법<br/><br/>
    1.실행 시 관리자 권한 오류 발생시 pycharm 관리자 권한으로 실행<br/>

    2.자동 로그인 설정 방법<br/>
![123123 (2)](https://user-images.githubusercontent.com/101561741/206841946-0960714a-6e9b-411e-a9e0-12354ccdf3e4.png)


 
 
    해당 부분 클릭 시 계좌를 설정하는 창이 나온다.<br/>
    창에 필요한 내용을 입력하면 기본 세팅이 완료된다.<br/>
    
    3. 실행 시 나오면 로그인<br/>

![캡처](https://user-images.githubusercontent.com/101561741/206842001-9c0f608b-9ebd-4877-b540-e7b5beb2cdfc.PNG)


    
    pytrader.py 실행 후 <br/>
    공동인증서 및 로그인 아이디 모두 입력


# 의존성<br/><br/>
    pyhon 3.9<br/>
    *키움증권 번개 api*<br/>
    *키움증권 오픈 api 모듈api*<br/>
    *Open API OCX 탑재 프로그램 제작 및 KOA Studioapi*<br/>
    *아나콘다 32bit *<br/>
    *Open API for Windows COM <br/>    
[키움증권사이트](https://www.kiwoom.com/h/common/event/VEventMainView?eventCode=20220074&from=138<br/>) *계좌개설 필요 *<br/>

***pip***<br/>

    pyqt 5.15.7<br/>
    pywin32 305<br/>
    pywinauto 0.6.8<br/>
    numpy 1.23.5<br/>
    kioom 1.3.1<br/>
    pandas 1.5.2<br/>
    sqlite 3.38.3<br/>

<br/><br/>
*****api*****
``` python 

class Kiwoom(QAxWidget): 
#QAxWidget 로 별도의 import 없이 키움api를 상속받게 해 줌


```

# 설치방법<br/><br/>
[키움증권 다운로드 사이트](https://www.kiwoom.com/h/customer/download/VOpenApiInfoView?dummyVal=0)<br/>

    0. 키움증권 회원가입/계좌개설/공동인증서 로그인<br/>
    1.오픈api 신청<br/>
    2.open api 모듈 다운로드<br/>
    3 번개 api 다운로드<br/>
    4.KOA Studio 다운로드<br/>
    5. 아나콘다 설치 후 32bit 변경<br/>

[설명해주는 사이트](https://losskatsu.github.io/it-infra/conda32/#4-%ED%82%A4%EC%9B%80-api-%EB%8B%A4%EC%9A%B4%EB%A1%9C%EB%93%9C)<br/>

    6. pip install <br/>
    pip install pyqt 5.15.7<br/>
    pip install pywin32 305<br/>
    pip install pywinauto 0.6.8<br/>
    pip install  numpy 1.23.5<br/>
    pip install  numpy 1.23.5<br/>
    pip install  kioom 1.3.1<br/>
    pip install  pandas 1.5.2<br/>
    pip install  sqlite<br/>


# lisence <br/>

    KIWOOM SECURITIES Corp. All Rights Reserved


# Contributer
    kim seung whan, lixxce5017@gmail.com,ChungBuk National Univ <br/>
    jun inwoo, wjsdlsdn1158@naver.com,ChungBuk National Univ<br/>
    lee seng min,lsm50399@naver.com, ChungBuk National Univ<br/>
