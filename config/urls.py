from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from Post.views.list import *
from Post.views.detail import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include('account.urls')),
    path('user/',include('users.urls')),

    # 특정 question 조회 url
    # Ex) 1번 질문 조회 : question/1/
    path('question/<int:question_pk>/', QuestionDetail.as_view(), name='question-detail'), #특정 질문 조회하기

    # answer 조회 및 작성
    path('answer/', AnswerList.as_view(), name='answer-list'),
    path('answer/<int:answer_pk>/', AnswerPutDeleteAPIView.as_view(), name='answer-detail'),

    # category 조회
    path('category/', CategoryList.as_view(), name='category-list'),

    # 언어별  조회
    # 전체 질문 조회 및 질문 만들기
    path('question/', QuestionList.as_view(), name='question-list'),
    # python 질문 조회
    path('python/question/', PythonList.as_view(), name='question-python'),
    # java 질문 조회
    path('java/question/', JavaList.as_view(), name='question-java'),
    # javascript 질문 조회
    path('javascript/question/', JavaScriptList.as_view(), name='question-javascript'),
    # C 질문 조회
    path('c/question/', CList.as_view(), name='question-c'),
    # C++ 질문 조회
    path('c++/question/', CCCList.as_view(), name='question-C++'),
    # Flutter 질문 조회
    path('flutter/question/', FlutterList.as_view(), name='question-flutter'),
    # Kotlin 질문 조회
    path('kotlin/question/', KotlinList.as_view(), name='question-kotlin'),
    # Swift 질문 조회
    path('swift/question/', SwiftList.as_view(), name='question-swift'),
    # Dart 질문 조회
    path('dart/question/', DartList.as_view(), name='question-dart'),
    # PHP 질문 조회
    path('php/question/', PHPList.as_view(), name='question-php'),
    # Typesciprt 질문 조회
    path('typescript/question/', TypeScriptList.as_view(), name='question-typescript'),
    # Go 질문 조회
    path('go/question/', GoList.as_view(), name='question-go'),

    # SQL
    # MySQL 질문 조회
    path('mysql/question/', MySQLList.as_view(), name='question-mysql'),
    # PostgreSQL 질문 조회
    path('postgresql/question/', PostgreSQLList.as_view(), name='question-postgresql'),
    # Maria DB 질문 조회
    path('mariadb/question/', MariaDBList.as_view(), name='question-mariadb'),
    # Oracle 질문 조회
    path('oracle/question/', OracleList.as_view(), name='question-oracle'),
    # MsSQL 질문 조회
    path('mssql/question/', MsSQLList.as_view(), name='question-mssql'),

    # NO SQL
    # Redis 질문 조회
    path('redis/question/', RedisList.as_view(), name='question-redis'),
    # MongoDB 질문 조회
    path('mongodb/question/', MongoDBList.as_view(), name='question-mongodb'),

    # CS / etc
    # CS 질문 조회
    path('cs/question/', CSList.as_view(), name='question-cs'),
    # etc 질문 조회
    path('etc/question/', EtcList.as_view(), name='question-etc'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
