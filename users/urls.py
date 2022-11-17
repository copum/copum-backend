from django.urls import path
from .views import getUserInfo

urlpatterns = [
    path('', views.getData),
    path('kakao/login/callback/', getUserInfo),
]