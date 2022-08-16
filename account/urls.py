
from django.urls import path, include
from . import kakaoapi
from apis import (
    LoginApi, 
    LogoutApi, 
    GoogleLoginApi, 
    GoogleSigninCallBackApi
)
from googleapi import *

urlpatterns = [
    path('kakao/login', kakaoapi.kakao),
    path('google/login', GoogleLoginApi.as_view(), name='google_login'),
    path('google/callback', GoogleSigninCallBackApi.as_view(), name='google_login_callback'),
    path('google/logout', LogoutApi.as_view(), name="logout"),
]