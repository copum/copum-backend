from urllib import parse

from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import *
from ..serializers import *


class QuestionList(APIView) :
    def get(self, request):
        question_search = request.GET.get('search', '')

        # key가 None이 아닐 경우 한글로 바꾸기
        for key in request.GET.keys():
            if request.GET.get(key) != None:
                parse.unquote(request.GET.get(key))

        # 검색할 내용이 title, body 다 없을 경우, 모든 질문 조회
        if question_search == '' :
            questions = Question.objects.order_by('-Question_created_at')

        # 검색할 내용이 title, body 해당하는 질문에 있는 경우
        else:
            queryset = Question.objects.filter(
                Q(Question_title__contains=question_search) | Q(Question_content__contains=question_search)
            )
            questions = queryset.order_by('-Question_created_at')

        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AnswerList(APIView) :
    def get(self, request):
        answers = Answer.objects.all()
        serializer = AnswerSerializer(answers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AnswerSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 카테고리 조회하기
class CategoryList(APIView) :
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# 언어 카테고리 별 조회하기
class PythonList(APIView) :
    def get(self, request):
        python_list = \
            Question.objects.filter(Question_category1=1) | \
            Question.objects.filter(Question_category2=1) | \
            Question.objects.filter(Question_category3=1) | \
            Question.objects.filter(Question_category4=1) \
        .order_by('-Question_created_at')
        serializer = QuestionSerializer(python_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class JavaList(APIView) :
    def get(self, request):
        java_list = Question.objects.filter(Question_category1=2) | \
                Question.objects.filter(Question_category2=2) | \
                Question.objects.filter(Question_category3=2) | \
                Question.objects.filter(Question_category4=2) \
                .order_by('-Question_created_at')
        serializer = QuestionSerializer(java_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class JavaScriptList(APIView) :
    def get(self, request):
        javascript_list = Question.objects.filter(Question_category1=3) | \
                Question.objects.filter(Question_category2=3) | \
                Question.objects.filter(Question_category3=3) | \
                Question.objects.filter(Question_category4=3) \
                .order_by('-Question_created_at')
        serializer = QuestionSerializer(javascript_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CList(APIView) :
    def get(self, request):
        c_list = Question.objects.filter(Question_category1=4) | \
                Question.objects.filter(Question_category2=4) | \
                Question.objects.filter(Question_category3=4) | \
                Question.objects.filter(Question_category4=4) \
                .order_by('-Question_created_at')
        serializer = QuestionSerializer(c_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CCCList(APIView) :
    def get(self, request):
        ccc_list = Question.objects.filter(Question_category1=5) | \
                   Question.objects.filter(Question_category2=5) | \
                   Question.objects.filter(Question_category3=5) | \
                   Question.objects.filter(Question_category4=5) \
                   .order_by('-Question_created_at')
        serializer = QuestionSerializer(ccc_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class FlutterList(APIView) :
    def get(self, request):
        flutter_list = Question.objects.filter(Question_category1=6) | \
                Question.objects.filter(Question_category2=6) | \
                Question.objects.filter(Question_category3=6) | \
                Question.objects.filter(Question_category4=6) \
                .order_by('-Question_created_at')
        serializer = QuestionSerializer(flutter_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class KotlinList(APIView) :
    def get(self, request):
        kotlin_list = Question.objects.filter(Question_category1=7) | \
                Question.objects.filter(Question_category2=7) | \
                Question.objects.filter(Question_category3=7) | \
                Question.objects.filter(Question_category4=7) \
                .order_by('-Question_created_at')
        serializer = QuestionSerializer(kotlin_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SwiftList(APIView) :
    def get(self, request):
        swift_list = Question.objects.filter(Question_category1=8) | \
                Question.objects.filter(Question_category2=8) | \
                Question.objects.filter(Question_category3=8) | \
                Question.objects.filter(Question_category4=8) \
                .order_by('-Question_created_at')
        serializer = QuestionSerializer(swift_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DartList(APIView) :
    def get(self, request):
        dart_list = Question.objects.filter(Question_category1=9) | \
                Question.objects.filter(Question_category2=9) | \
                Question.objects.filter(Question_category3=9) | \
                Question.objects.filter(Question_category4=9) \
                .order_by('-Question_created_at')
        serializer = QuestionSerializer(dart_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PHPList(APIView) :
    def get(self, request):
        php_list = Question.objects.filter(Question_category1=10) | \
                Question.objects.filter(Question_category2=10) | \
                Question.objects.filter(Question_category3=10) | \
                Question.objects.filter(Question_category4=10) \
                .order_by('-Question_created_at')
        serializer = QuestionSerializer(php_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TypeScriptList(APIView) :
    def get(self, request):
        typescript_list = Question.objects.filter(Question_category1=11) | \
                Question.objects.filter(Question_category2=11) | \
                Question.objects.filter(Question_category3=11) | \
                Question.objects.filter(Question_category4=11) \
                .order_by('-Question_created_at')
        serializer = QuestionSerializer(typescript_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GoList(APIView) :
    def get(self, request):
        go_list = Question.objects.filter(Question_category1=12) | \
                Question.objects.filter(Question_category2=12) | \
                Question.objects.filter(Question_category3=12) | \
                Question.objects.filter(Question_category4=12) \
                .order_by('-Question_created_at')
        serializer = QuestionSerializer(go_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# SQL 카테고리 조회하기
class MySQLList(APIView) :
    def get(self, request):
        mysql_list = Question.objects.filter(Question_category1=13) | \
            Question.objects.filter(Question_category2=13) | \
            Question.objects.filter(Question_category3=13) | \
            Question.objects.filter(Question_category4=13)\
            .order_by('-Question_created_at')
        serializer = QuestionSerializer(mysql_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PostgreSQLList(APIView) :
    def get(self, request):
        postgresql_list = Question.objects.filter(Question_category1=14) | \
                Question.objects.filter(Question_category2=14) | \
                Question.objects.filter(Question_category3=14) | \
                Question.objects.filter(Question_category4=14) \
                .order_by('-Question_created_at')
        serializer = QuestionSerializer(postgresql_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MariaDBList(APIView) :
    def get(self, request):
        mariadb_list = Question.objects.filter(Question_category1=15) | \
                Question.objects.filter(Question_category2=15) | \
                Question.objects.filter(Question_category3=15) | \
                Question.objects.filter(Question_category4=15) \
                .order_by('-Question_created_at')
        serializer = QuestionSerializer(mariadb_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class OracleList(APIView) :
    def get(self, request):
        oracle_list = Question.objects.filter(Question_category1=16) | \
                Question.objects.filter(Question_category2=16) | \
                Question.objects.filter(Question_category3=16) | \
                Question.objects.filter(Question_category4=16) \
                .order_by('-Question_created_at')
        serializer = QuestionSerializer(oracle_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MsSQLList(APIView) :
    def get(self, request):
        mssql_list = Question.objects.filter(Question_category1=17) | \
                Question.objects.filter(Question_category2=17) | \
                Question.objects.filter(Question_category3=17) | \
                Question.objects.filter(Question_category4=17) \
                .order_by('-Question_created_at')
        serializer = QuestionSerializer(mssql_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


#NoSQL 카테고리 조회하기
class RedisList(APIView) :
    def get(self, request):
        redis_list = Question.objects.filter(Question_category1=18) | \
                Question.objects.filter(Question_category2=18) | \
                Question.objects.filter(Question_category3=18) | \
                Question.objects.filter(Question_category4=18) \
                .order_by('-Question_created_at')
        serializer = QuestionSerializer(redis_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MongoDBList(APIView) :
    def get(self, request):
        mongodb_list = Question.objects.filter(Question_category1=19) | \
                Question.objects.filter(Question_category2=19) | \
                Question.objects.filter(Question_category3=19) | \
                Question.objects.filter(Question_category4=19) \
                .order_by('-Question_created_at')
        serializer = QuestionSerializer(mongodb_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# CS 카테고리 조회하기
class CSList(APIView) :
    def get(self, request):
        cs_list = Question.objects.filter(Question_category1=20) | \
                Question.objects.filter(Question_category2=20) | \
                Question.objects.filter(Question_category3=20) | \
                Question.objects.filter(Question_category4=20) \
                .order_by('-Question_created_at')
        serializer = QuestionSerializer(cs_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# etc 카테고리 조회하기
class EtcList(APIView) :
    def get(self, request):
        etc_list = Question.objects.filter(Question_category1=21) | \
                Question.objects.filter(Question_category2=21) | \
                Question.objects.filter(Question_category3=21) | \
                Question.objects.filter(Question_category4=21) \
                    .order_by('-Question_created_at')
        serializer = QuestionSerializer(etc_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)