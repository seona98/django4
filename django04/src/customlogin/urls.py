from customlogin.views import *
from django.urls import path

app_name='cl'
#도메인 주소: 127.0.0.1:8000/login/
urlpatterns=[
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('signout/', signout, name='signout')
    ]