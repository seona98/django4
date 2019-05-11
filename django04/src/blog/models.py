from django.db import models
from django.contrib.auth.models import User

#카테고리
#카테고리명
class Category(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name
    
#글
#카테고리-왜래키, 제목, 글쓴이-외래키, 글내용, 작성일
class Post(models.Model):
    c = models.ForeignKey(Category, on_delete=models.PROTECT)
    title = models.CharField(max_length=200)
    u = models.ForeignKey(User, on_delete = models.CASCADE)
    #TextField: 글자수 제한이 없는 저장공간을 설정하는 클래스
    #null: 데이터베이스에 해당 변수값이 없어도 저장되도록 설정하는 매개변수
    #blank: 사용자가 입력양식에 해당 변수값을 빈칸으로 둬도 폼을 서버에 전달할 수 있도록 설정하는 매개변수
    #null과 blank 매개변수는 모든 Field클래스에서 사용할 수 있음
    content = models.TextField(null=True, blank=True)
    #auto_now_add(DateTimeField나 DateField에서 사용가능)
    #: 객체 생성시, 서버 기준의 날짜/시간이 자동으로 입력되도록 설정하는 매개변수
    pub_date = models.DateTimeField(auto_now_add=True)
    
#글의 첨부파일
#글-외래키, 파일저장공간
class PostFile(models.Model):
    p = models.ForeignKey(Post, on_delete= models.CASCADE)
    #FileField: 모든 파일을 서버 하드디스크에 저장하는 공간
    #upload_to: 객체 생성 중 FileField에 저장한 파일이 실제로 서버 하드디스크에 저장되는 경로
    f = models.FileField(upload_to='files/')
    
#글의 이미지파일
#글-외래키, 이미지파일 저장공간 
class PostImage(models.Model):
    p = models.ForeignKey(Post, on_delete=models.CASCADE)
    #ImageField: 이미지 파일을 서버 하드디스크에 저장하는 클래스
    #단, 해당 필드를 사용하려면 Pillow 모듈이 파이썬에 설치가 되어있어야 함
    #pillow: python에서 이미지 처리에 사용되는 대표적인 라이브러리
    i = models.ImageField(upload_to = 'images/')











