****주식 추천 프로그램****<br/>
**산업스파이**<br/><br/><br/><br/>

# 서비스 소개<br/><br/>
  
# 실행 방법<br/><br/>

# 의존성<br/><br/>
pyhon 3.9<br/>
*키움증권 번개 api*<br/>
[키움증권사이트](https://www.kiwoom.com/h/common/event/VEventMainView?eventCode=20220074&from=138<br/>) *계좌개설 필요 *<br/>
키움증권 오픈 api 모듈api*<br/>
Open API OCX 탑재 프로그램 제작 및 KOA Studioapi*<br/>
아나콘다 32bit *<br/>
Open API for Windows COM <br/>

***pip***<br/>
pyqt 5.15.7
pywin32 305
pywinauto 0.6.8
numpy 1.23.5
kioom 1.3.1
pandas 1.5.2
sqlite 3.38.3

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

6. pip install 
pip install pyqt 5.15.7
pip install pywin32 305
pip install pywinauto 0.6.8
pip install  numpy 1.23.5
pip install  numpy 1.23.5
pip install  kioom 1.3.1
pip install  pandas 1.5.2
pip install  sqlite


# lisence 


# Contributer
kim seung whan, lixxce5017@gmail.com,ChungBuk National Univ <br/>
jun inwoo, wjsdlsdn1158@naver.com,ChungBuk National Univ<br/>
lee seng min, ChungBuk National Univ<br/>
