
from django.urls import path, include
from . import kakaoapi, googleapi


urlpatterns = [
    path('kakao/login', kakaoapi.kakao_login.as_view()),
    path('google/login', googleapi.google_login),
]