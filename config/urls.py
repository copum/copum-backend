from django.contrib import admin
from django.urls import path, include, re_paths
from Post.views.list import *
from Post.views.detail import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include('account.urls')),
    path('user/',include('users.urls')),
    path('category/',include('Category.urls')),

    #question 조회 url
    path('question/', QuestionList.as_view(), name='question-list'),
    path('question/<int:pk>/', QuestionDetail.as_view(), name='question-detail')
]
