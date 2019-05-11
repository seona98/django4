'''
Created on 2019. 4. 21.

@author: 405-13
'''

'''
어플리케이션 별로 별도의 URL Conf를 만들 수 있음
단, app_name과 urlpatterns 변수를 정의해야함(이름이 틀리면 URL Conf가 설정되지 않음)
app_name: 이 파일에 정의한 URL들의 그룹이름(문자열)
urlpatterns: path함수를 이용해 뷰함수를 등록하는 변수(리스트)
만들어진 urls.py를 프로젝트 폴더의 urls.py에 알려줘야 함.
'''
from django.urls import path
from vote.views import *

app_name = 'vote'
#기본 도메인 주소: 127.0.0.1:8000/vote/
urlpatterns = [
    #127.0.0.1:8000/vote/ 요청이 들어오면 index함수 호출
    path('', index),
    #127.0.0.1:8000/vote/숫자값 요청이 들어오면 detail함수 호출
    #숫자값은 q_id 매개변수에 값으로 사용됨
    path('<int:q_id>/', detail),
    #127.0.0.1:8000/vote/vote/ -> vote함수 호출
    path('vote/', vote),
    #127.0.0.1:8000/vote/result/숫자값/ -> result함수 호출
    path('result/<int:q_id>/', result),
    #127.0.0.1:8000/vote/qr/ -> qregiste함수 호출
    #파이썬코드가 HTML에서 vote:qr 별칭으로 URL을 찾을 수 있음
    path('qr/', qregiste, name='qr'),
    #127.0.0.1:8000/vote/qr/ -> qregiste함수 호출
    #파이썬코드가 HTML에서 vote:cr 별칭으로 URL을 찾을 수 있음
    path('cr/', cregiste, name='cr'),
    path('<int:q_id>/change/', qupdate, name='qu'),
    path('<int:q_id>/qdelete/', qdelete, name='qd'),
    path('<int:c_id>/cupdate/', cupdate, name='cu'),
    path('<int:c_id>/cdelete/', cdelete, name='cd')
    ]
















