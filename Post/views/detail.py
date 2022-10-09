from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from apptest.models import Question, Answer
from apptest.serializer import QuestionSerializer, QuestionDetailSerializer, AnswerSerializer


class QuestionDetail(APIView) :
    def get(self, request, pk):
        question = get_object_or_404(Question, Question_id = pk)
        serializer = QuestionDetailSerializer(question)
        return Response(serializer.data,  status=status.HTTP_200_OK)

    def put(self, request, pk):
        question = get_object_or_404(Question, Question_id = pk)
        serializer = QuestionDetailSerializer(question, data = request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        question = get_object_or_404(Question, Question_id = pk)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
