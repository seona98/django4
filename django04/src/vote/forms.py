'''
Form: django에서 HTML코드에 들어갈 <imput>태그를 파이썬 코드 형태로 관리할 수 있도록 제공하는 기능

Form은 모델클래스를 기반으로 입력공간을 생성할 수도 있고, 커스텀 입력양식을 생성할 수도 있음
ModelForm: 모델클래스와 연동된 폼을 만들 때 상속받는 클래스
Form: 커스텀 입력양식으로만 폼을 만들 때 상속받는 클래스

장점
Model클래스에 변동사항을 자동으로 Form클래스가 인지해서 사용자에가 입력할 수 있는 공간을 변경해줌
디자이너가 직접 입력양식을 만들지 않아도 됨
'''

from django.forms.models import ModelForm
from vote.models import Question, Choice

#Question 모델클래스와 연동된 모델폼클래스 정의
#클라이언트가 Question 객체를 추가/수정할 때 사용
class QuestionForm(ModelForm):
    #Meta 클래스: 연동하고자 하는 모델클래스에 대한 정보를 정의하는 클래스
    class Meta:
        #model, fields, exclude, forms, widgets
        #model: 연동할 모델클래스 이름을 저장하는 변수
        model = Question
        #fields: 사용자가 입력할 수 있는 <input>태그를 생성할 때, 모델클래스에 정의된 변수들 중 어떤 변수를 클라이언트에게 제공할 것인지 지정
        #exclude: 모델클래스에 정의된 변수 중 어떤 변수를 제외하고 클라이언트에게 제공할 것인지 지정
        #변수이름은 문자열 형태로, 저장하는 타입은 리스트형태로
        #fields나 exclude 변수 중 한 개만 사용
        fields = ['name']
        #exclude = ['pub_date']
#Choice 모델클래스와 연동된 모델폼클래스 정의
#클라이언트가 Choice 객체를 추가/수정할 때 사용
class ChoiceForm(ModelForm):
    class Meta:
        model = Choice
        fields = ['q', 'name']
        #exclude = ['votes']























