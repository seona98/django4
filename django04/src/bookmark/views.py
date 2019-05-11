from django.shortcuts import render
'''
자동 임포트된 render(HTML 파일 보낼 대상, 보낼 HTML 파일, HTML 파일을 수정할 때 사용할 값)
: 웹 클라이언트에게 HTML 파일을 전달할 때 사용하는 함수
render 결과값으로는 HTML 코드 문자열이 반환됨. 따라서 return 키워드에 render 함수 호출로 사용자에게 HTML파일을 전달할 수 있음

views.py: MTV 패턴 중 View의 기능을 하는 클래스/함수를 정의하는 공간
뷰 함수를 정의할 때, 첫 번째 매개변수로 request를 사용해야 함.
request: 웹 클라이언트에 대한 정보(요청 정보, <form>으로 넘겨준 데이터, 로그인 정보, 세션 정보, 요청 방식)을 저장한 변수

'''
#메인화면
def main(request):
    #웹 클라이언트에게 main.html을 전달함.
    #전달하기 전에 a변수와 b변수로 main.html을 수정함
    #수정할 때 사용할 값을 사전형으로 정의할 수 있고, key에 해당하는 문자열이 html파일 내에서 변수이름으로 사용됨
    return render(request, 'main.html', {'a' : 10, 'b':[1,2,3]})

#Bookmark 모델 클래스 임포트
from bookmark.models import Bookmark
#데이터베이스에 저장된 Bookmark 객체 기반의 HTML화면
def booklist(request):
    '''
    모델클래스를 통해 데이터베이스에 저장된 객체 가져오기
    Bookmark.objects.all(): 데이터베이스에 해당 모델클래스의 모든 객체 추출(리스트)
    Bookmark.objects.get(조건): 데이터베이스에 해당 모델클래스 객체 중 조건에 맞는 객체 한 개를 추출(객체)
    Bookmark.objects.filter(조건): 데이터베이스에 해당 모델클래스의 객체 중 조건에 맞는 객체들을 추출(리스트)
    Bookmark.object.exclude(조건): 데이터베이스에 해당 모델클래스의 객체 중 조건에 맞지 않는 객체들을 추출(리스트)
    '''
    #데이터베이스에 저장된 Bookmark 객체 모두 추출
    objs = Bookmark.objects.all()
    print(objs)
    #HTML 파일을 전달하면서 Bookmark 객체로 HTML 편집
    return render(request, 'booklist.html', {'list': objs})
    
#Bookmark 객체 중 하나를 선택한 HTML화면
#request 외에 매개변수 추가시, URL에서 데이터를 추출해 사용하는 것을 의미
#-> url 등록시, 어떤 공간에 작성된 데이터를 매개변수에 넘겨줄지 지정해야함
def getBook(request, book_id):
    #Bookmark 객체들 중 book_id와 같은 id값을 가진 객체 한 개를 추출
    a = Bookmark.objects.get(id=book_id)
    print(a)
    #결과값을 HTML수정할 때 사용하도록 전달
    return render(request, 'getBook.html', {'obj': a})
    









