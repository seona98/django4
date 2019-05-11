'''
Created on 2019. 5. 4.

@author: 405-13
'''
from django.urls import path
from blog.views import *
app_name='blog'
urlpatterns=[
    #뷰클래스를 url 등록시, 뷰클래스.as_view()함수로 등록함
    path('', Index.as_view(), name='index'),
    #DetailView를 상속받은 클래스뷰는 pk매개변수에 id변수값을 넘겨줘야함
    path('<int:pk>/', Detail.as_view(), name='detail'),
    path('posting/', Posting.as_view(), name='posting'),
    path('search/', PostSearch.as_view(), name='postsearch')
    ]
