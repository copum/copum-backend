from urllib import parse

from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import *
from ..serializers import *


class QuestionList(APIView) :
    def get(self, request):
        search_category1 = request.GET.get('category1')
        search_category2 = request.GET.get('category2')
        search_category3 = request.GET.get('category3')
        search_category4 = request.GET.get('category4')
        search_title = request.GET.get('title')

        # key가 None이 아닐 경우 한글로 바꾸기
        for key in request.GET.keys():
            if request.GET.get(key) != None:
                parse.unquote(request.GET.get(key))

        # category1, 2, 3, 4, title 다 없을 경우, 모든 질문 조회
        if (search_category1 == None) & (search_category2 == None) & (search_category3 == None) \
                & (search_category4 == None) & (search_title == None):
            questions = Question.objects.order_by('-Question_created_at')

        # title이 있는 경우
        elif search_title:
            queryset = Question.objects.filter(
                Q(Question_category1=search_category1) | Q(Question_category1=search_category2) | \
                Q(Question_category1=search_category3) | Q(Question_category1=search_category4) | \

                Q(Question_category2=search_category1) | Q(Question_category2=search_category2) | \
                Q(Question_category2=search_category3) | Q(Question_category2=search_category4) | \

                Q(Question_category3=search_category1) | Q(Question_category3=search_category2) | \
                Q(Question_category3=search_category3) | Q(Question_category3=search_category4) | \

                Q(Question_category4=search_category1) | Q(Question_category4=search_category2) | \
                Q(Question_category4=search_category3) | Q(Question_category4=search_category4) | \

                Q(Question_title__contains=search_title)
            )
            questions = queryset.order_by('-Question_created_at')

        # category1, 2, 3, 4, title 중 하나가 있을 경우
        else:
            queryset = Question.objects.filter(
                Q(Question_category1=search_category1) | Q(Question_category1=search_category2) | \
                Q(Question_category1=search_category3) | Q(Question_category1=search_category4) | \

                Q(Question_category2=search_category1) | Q(Question_category2=search_category2) | \
                Q(Question_category2=search_category3) | Q(Question_category2=search_category4) | \

                Q(Question_category3=search_category1) | Q(Question_category3=search_category2) | \
                Q(Question_category3=search_category3) | Q(Question_category3=search_category4) | \

                Q(Question_category4=search_category1) | Q(Question_category4=search_category2) | \
                Q(Question_category4=search_category3) | Q(Question_category4=search_category4) | \

                Q(Question_title=search_title)
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

# 언어 카테고리 별 조회하기
class PythonList(APIView) :
    def get(self, request):
        python_list = Question.objects.filter(Question_category1=CategoryType.Python) | \
            Question.objects.filter(Question_category2=CategoryType.Python) | \
            Question.objects.filter(Question_category3=CategoryType.Python)| \
            Question.objects.filter(Question_category4=CategoryType.Python) \
            .order_by('-Question_created_at')
        serializer = QuestionSerializer(python_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class JavaList(APIView) :
    def get(self, request):
        java_list = Question.objects.filter(Question_category1=CategoryType.Java) | \
                Question.objects.filter(Question_category2=CategoryType.Java) | \
                Question.objects.filter(Question_category3=CategoryType.Java) | \
                Question.objects.filter(Question_category4=CategoryType.Java) \
                .order_by('-Question_created_at')
        serializer = QuestionSerializer(java_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class JavaScriptList(APIView) :
    def get(self, request):
        javascript_list = Question.objects.filter(Question_category1=CategoryType.JavaScript) | \
                Question.objects.filter(Question_category2=CategoryType.JavaScript) | \
                Question.objects.filter(Question_category3=CategoryType.JavaScript) | \
                Question.objects.filter(Question_category4=CategoryType.JavaScript) \
                .order_by('-Question_created_at')
        serializer = QuestionSerializer(javascript_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CList(APIView) :
    def get(self, request):
        c_list = Question.objects.filter(Question_category1=CategoryType.C) | \
                Question.objects.filter(Question_category2=CategoryType.C) | \
                Question.objects.filter(Question_category3=CategoryType.C) | \
                Question.objects.filter(Question_category4=CategoryType.C) \
                .order_by('-Question_created_at')
        serializer = QuestionSerializer(c_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CCCList(APIView) :
    def get(self, request):
        ccc_list = Question.objects.filter(Question_category1=CategoryType.CCC) | \
                   Question.objects.filter(Question_category2=CategoryType.CCC) | \
                   Question.objects.filter(Question_category3=CategoryType.CCC) | \
                   Question.objects.filter(Question_category4=CategoryType.CCC) \
                   .order_by('-Question_created_at')
        serializer = QuestionSerializer(ccc_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class FlutterList(APIView) :
    def get(self, request):
        flutter_list = Question.objects.filter(Question_category1=CategoryType.Flutter) | \
                Question.objects.filter(Question_category2=CategoryType.Flutter) | \
                Question.objects.filter(Question_category3=CategoryType.Flutter) | \
                Question.objects.filter(Question_category4=CategoryType.Flutter) \
                .order_by('-Question_created_at')
        serializer = QuestionSerializer(flutter_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class KotlinList(APIView) :
    def get(self, request):
        kotlin_list = Question.objects.filter(Question_category1=CategoryType.Kotlin) | \
                Question.objects.filter(Question_category2=CategoryType.Kotlin) | \
                Question.objects.filter(Question_category3=CategoryType.Kotlin) | \
                Question.objects.filter(Question_category4=CategoryType.Kotlin) \
                .order_by('-Question_created_at')
        serializer = QuestionSerializer(kotlin_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SwiftList(APIView) :
    def get(self, request):
        swift_list = Question.objects.filter(Question_category1=CategoryType.Swift) | \
                Question.objects.filter(Question_category2=CategoryType.Swift) | \
                Question.objects.filter(Question_category3=CategoryType.Swift) | \
                Question.objects.filter(Question_category4=CategoryType.Swift) \
                .order_by('-Question_created_at')
        serializer = QuestionSerializer(swift_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DartList(APIView) :
    def get(self, request):
        dart_list = Question.objects.filter(Question_category1=CategoryType.Dart) | \
                Question.objects.filter(Question_category2=CategoryType.Dart) | \
                Question.objects.filter(Question_category3=CategoryType.Dart) | \
                Question.objects.filter(Question_category4=CategoryType.Dart) \
                .order_by('-Question_created_at')
        serializer = QuestionSerializer(dart_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PHPList(APIView) :
    def get(self, request):
        php_list = Question.objects.filter(Question_category1=CategoryType.PHP) | \
                Question.objects.filter(Question_category2=CategoryType.PHP) | \
                Question.objects.filter(Question_category3=CategoryType.PHP) | \
                Question.objects.filter(Question_category4=CategoryType.PHP) \
                .order_by('-Question_created_at')
        serializer = QuestionSerializer(php_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TypeScriptList(APIView) :
    def get(self, request):
        typescript_list = Question.objects.filter(Question_category1=CategoryType.TypeScript) | \
                Question.objects.filter(Question_category2=CategoryType.TypeScript) | \
                Question.objects.filter(Question_category3=CategoryType.TypeScript) | \
                Question.objects.filter(Question_category4=CategoryType.TypeScript) \
                .order_by('-Question_created_at')
        serializer = QuestionSerializer(typescript_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GoList(APIView) :
    def get(self, request):
        go_list = Question.objects.filter(Question_category1=CategoryType.Go) | \
                Question.objects.filter(Question_category2=CategoryType.Go) | \
                Question.objects.filter(Question_category3=CategoryType.Go) | \
                Question.objects.filter(Question_category4=CategoryType.Go) \
                .order_by('-Question_created_at')
        serializer = QuestionSerializer(go_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# SQL 카테고리 조회하기
class MySQLList(APIView) :
    def get(self, request):
        mysql_list = Question.objects.filter(Question_category1=CategoryType.MySQL) | \
            Question.objects.filter(Question_category2=CategoryType.MySQL) | \
            Question.objects.filter(Question_category3=CategoryType.MySQL) | \
            Question.objects.filter(Question_category4=CategoryType.MySQL)\
            .order_by('-Question_created_at')
        serializer = QuestionSerializer(mysql_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PostgreSQLList(APIView) :
    def get(self, request):
        postgresql_list = Question.objects.filter(Question_category1=CategoryType.PostgreSQL) | \
                Question.objects.filter(Question_category2=CategoryType.PostgreSQL) | \
                Question.objects.filter(Question_category3=CategoryType.PostgreSQL) | \
                Question.objects.filter(Question_category4=CategoryType.PostgreSQL) \
                .order_by('-Question_created_at')
        serializer = QuestionSerializer(postgresql_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MariaDBList(APIView) :
    def get(self, request):
        mariadb_list = Question.objects.filter(Question_category1=CategoryType.MariaDB) | \
                Question.objects.filter(Question_category2=CategoryType.MariaDB) | \
                Question.objects.filter(Question_category3=CategoryType.MariaDB) | \
                Question.objects.filter(Question_category4=CategoryType.MariaDB) \
                .order_by('-Question_created_at')
        serializer = QuestionSerializer(mariadb_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class OracleList(APIView) :
    def get(self, request):
        oracle_list = Question.objects.filter(Question_category1=CategoryType.Oracle) | \
                Question.objects.filter(Question_category2=CategoryType.Oracle) | \
                Question.objects.filter(Question_category3=CategoryType.Oracle) | \
                Question.objects.filter(Question_category4=CategoryType.Oracle) \
                .order_by('-Question_created_at')
        serializer = QuestionSerializer(oracle_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MsSQLList(APIView) :
    def get(self, request):
        mssql_list = Question.objects.filter(Question_category1=CategoryType.MsSQL) | \
                Question.objects.filter(Question_category2=CategoryType.MsSQL) | \
                Question.objects.filter(Question_category3=CategoryType.MsSQL) | \
                Question.objects.filter(Question_category4=CategoryType.MsSQL) \
                .order_by('-Question_created_at')
        serializer = QuestionSerializer(mssql_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


#NoSQL 카테고리 조회하기
class RedisList(APIView) :
    def get(self, request):
        redis_list = Question.objects.filter(Question_category1=CategoryType.Redis) | \
                Question.objects.filter(Question_category2=CategoryType.Redis) | \
                Question.objects.filter(Question_category3=CategoryType.Redis) | \
                Question.objects.filter(Question_category4=CategoryType.Redis) \
                .order_by('-Question_created_at')
        serializer = QuestionSerializer(redis_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MongoDBList(APIView) :
    def get(self, request):
        mongodb_list = Question.objects.filter(Question_category1=CategoryType.MongoDB) | \
                Question.objects.filter(Question_category2=CategoryType.MongoDB) | \
                Question.objects.filter(Question_category3=CategoryType.MongoDB) | \
                Question.objects.filter(Question_category4=CategoryType.MongoDB) \
                .order_by('-Question_created_at')
        serializer = QuestionSerializer(mongodb_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# CS 카테고리 조회하기
class CSList(APIView) :
    def get(self, request):
        cs_list = Question.objects.filter(Question_category1=CategoryType.CS) | \
                Question.objects.filter(Question_category2=CategoryType.CS) | \
                Question.objects.filter(Question_category3=CategoryType.CS) | \
                Question.objects.filter(Question_category4=CategoryType.CS) \
                .order_by('-Question_created_at')
        serializer = QuestionSerializer(cs_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# etc 카테고리 조회하기
class EtcList(APIView) :
    def get(self, request):
        etc_list = Question.objects.filter(Question_category1=CategoryType.etc) | \
                Question.objects.filter(Question_category2=CategoryType.etc) | \
                Question.objects.filter(Question_category3=CategoryType.etc) | \
                Question.objects.filter(Question_category4=CategoryType.etc) \
                    .order_by('-Question_created_at')
        serializer = QuestionSerializer(etc_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)