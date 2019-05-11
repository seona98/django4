from django.db import models

'''
models.py: 해당 어플리케이션에서 데이터베이스에 저장할 데이터 형태를 정의하는 공간
자동 임포트된 models라는  파이썬 파일에는 모델클래스를 정의할 때 필요한 클래스, 함수가 정의됨

models 클래스 개발 및 웹 프로젝트 반영 순서
1) 모델 클래스를 정의하면서 models.Model 클래스를 상속
2) 모델 클래스에서 저장할 값의 타입과 이름을 클래스 변수로 지정
3) 정의된 모델클래스를  migration 파일로 변환
4) migration 파일을 웹프로젝트에 반영(migrate)

models.XXXXField: 클래스 변수에 어떤 형태의 값을 저장하도록 정의할지 객체를 생성할 때 사용하는 클래스
models.CharField: 글자수 제한이 있는 문자열을 저장할 때 사용하는 클래스
필수 매개변수로 max_length라는 최대 글자수 길이를 입력해야함
models.URLField: 인터넷 주소(URL)을 저장할 때 사용하는 클래스
'''

#북마트 모델클래스
#즐겨찾기 이름(문자열), 클릭시 이동할 사이트 주소(url)
class Bookmark(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField()
    #__str__: 객체를 화면에 출력할 때 어떤 형태로 띄울지 정의된 함수
    def __str__(self):
        return self.name