'''
Created on 2019. 4. 28.

@author: 405-13
'''
#django에서 기본적으로 제공하는 회원관리 어플리케이션
#그 어플리케이션에 있는 models.py에 접근해 User(회원) 클래스 임포트
from django.contrib.auth.models import User
from django import forms
#회원가입에 사용할 폼
#아이디, 비밀번호, 비밀번호 확인, 성, 이름, 이메일
'''
모델클래스에 없는 입력양식 생성
forms.py에 들어있는 XXXFields 객체를 클래스 변수에 저장해서 구현
모델클래스에서 사용했던 클래스이름과 유사하나, 내부기능이 다르기때문에 주의해야함
models.XXXField: 데이터베이스에 어떤 데이터를 저장할 지 지정하는 클래스
forms.XXXField: <input>태그를 만들 때 어떤 형식으로 제공할지 지정하는 클래스

forms.XXXInput: <input>태그에 입력 형식을 바꿀 수 있는 클래스로 widget 매개변수(모델클래스와 연동한 경우 widgets)에 지정할 수 있음
forms.PasswordInput: 텍스트 형태의 입력을 패스워드 형식으로 바꿔주는 위젯
'''
class SignupForm(forms.models.ModelForm):
    #label: HTML코드로 변환할 때, <label>태그 안에 들어갈 설명을 지정할 수 있는 변수
    #widget: HTML코드로 변환할 때, type 속성값을 위젯으로 변환할 때 사용하는 변수
    password_check = forms.CharField(widget=forms.PasswordInput(), label="비밀번호 확인", max_length=128)
    
    #field_order: 입력양식의 순서를 저장하는 변수. 리스트타입으로 변수명을 문자열로 저장
    field_order = ['username', 'password', 'password_check', 'last_name', 'first_name', 'email']
    
    class Meta:
        model = User
        fields = ['username', 'password', 'last_name', 'first_name', 'email']
        #widgets: 모델클래스의 변수에 위젯을 적용할 때 사용하는 변수(사전형)
        #키 부분에 변수이름을 문자열로, 값 부분에 위젯 객체를 저장
        widgets = {
            'password': forms.PasswordInput()
            }

#로그인에 사용할 폼
#아이디, 비밀번호
class SigninForm(forms.models.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {'password': forms.PasswordInput()}


































