
from django.urls import path, include
from . import kakaoapi, googleapi
from googleapi import *

urlpatterns = [
    path('kakao/login', kakaoapi.kakao),
    path('google/login', googleapi.google),
]