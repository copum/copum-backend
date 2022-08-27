
from django.urls import path, include
from . import kakaoapi, googleapi
from googleapi import *

urlpatterns = [
    path('kakao/login', kakaoapi.kakao_login),
    path('google/login', googleapi.google_login),
]