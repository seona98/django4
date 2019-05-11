from django import forms
from blog.models import Post


#글쓰기에 사용할 폼클래스 - Post 모델클래스 연동
#Post 모델 클래스에 변수 외에 PostImage, PostFile 객체 생성에 사용할 첨부파일 입력 공간 생성
class PostingForm(forms.ModelForm):
    #required: 사용자가 반드시 입력해야하는 입력양식을 설정할 때 사용하는 매개변수
    #required에 기본값은 True. True인 경우 사용자가 반드시 값을 입력해야함
    #False인 경우 사용자가 해당 입력공간을 입력하지 않아도 됨
    #ClearableFileInput: HTML코드 기준 <input type=File>인 입력공간에 별도의 속성을 설정할 때 사용하는 위젯
    files = forms.FileField(label = '첨부파일', required=False, 
                            widget=forms.ClearableFileInput(attrs={'multiple':True}))
    images = forms.ImageField(label = '이미지', required=False, 
                            widget=forms.ClearableFileInput(attrs={'multiple':True}))
    class Meta:
        model = Post
        fields = ['c', 'title', 'content']
        #exclude = ['u', 'pub_date']
