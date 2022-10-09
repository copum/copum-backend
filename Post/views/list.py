from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import *
from ..serializers import *


class QuestionList(APIView) :
    def get(self, request):
        question_list = Question.objects.all()
        serializer = QuestionSerializer(question_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



