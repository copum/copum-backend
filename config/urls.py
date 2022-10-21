from django.contrib import admin
from django.urls import path, include
from Post.views.list import *
from Post.views.detail import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include('account.urls')),
    path('user/',include('users.urls')),

    #question 조회 url
    path('question/<int:question_pk>/', QuestionDetail.as_view(), name='question-detail'), #특정 질문 조회하기

    # answer 조회 및 작성
    path('answer/', AnswerList.as_view(), name='answer-list'),
    path('answer/<int:answer_pk>/', AnswerPutDeleteAPIView.as_view(), name='answer-detail'),

    # 언어 조회
    path('question/', QuestionList.as_view(), name='question-list'), # 모든 질문 조회
    path('python/question/', PythonList.as_view(), name='question-python'),  # python 질문 조회
    path('java/question/', JavaList.as_view(), name='question-java'),  # java 질문 조회
    path('javascript/question/', JavaScriptList.as_view(), name='question-javascript'),
    path('c/question/', CList.as_view(), name='question-c'),
    path('c++/question/', CCCList.as_view(), name='question-C++'),
    path('flutter/question/', FlutterList.as_view(), name='question-flutter'),
    path('kotlin/question/', KotlinList.as_view(), name='question-kotlin'),
    path('swift/question/', SwiftList.as_view(), name='question-swift'),
    path('dart/question/', DartList.as_view(), name='question-dart'),
    path('php/question/', PHPList.as_view(), name='question-php'),
    path('typescript/question/', TypeScriptList.as_view(), name='question-typescript'),
    path('go/question/', GoList.as_view(), name='question-go'),

    # SQL
    path('mysql/question/', MySQLList.as_view(), name='question-mysql'),
    path('postgresql/question/', PostgreSQLList.as_view(), name='question-postgresql'),
    path('mariadb/question/', MariaDBList.as_view(), name='question-mariadb'),
    path('oracle/question/', OracleList.as_view(), name='question-oracle'),
    path('mssql/question/', MsSQLList.as_view(), name='question-mssql'),
    # NO SQL
    path('redis/question/', RedisList.as_view(), name='question-redis'),
    path('mongodb/question/', MongoDBList.as_view(), name='question-mongodb'),

    # CS
    path('cs/question/', CSList.as_view(), name='question-cs'),
    # etc
    path('etc/question/', EtcList.as_view(), name='question-etc'),
]
