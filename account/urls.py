from django.urls import path
from .kakaoapi import kakao_login


urlpatterns = [
    path('kakao/login', kakao_login.as_view()),
    # path('google/login', googleapi.google_login),
]
