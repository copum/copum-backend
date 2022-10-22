from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from Post.models import Question, Answer
from Post.serializers import QuestionSerializer, QuestionDetailSerializer, AnswerSerializer


class QuestionDetail(APIView) :
    def get(self, request, question_pk):
        question = get_object_or_404(Question, pk=question_pk)
        serializer = QuestionDetailSerializer(question)
        if request.user:
            question.Question_counting += 0
        else:
            question.Question_counting += 1
        question.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, question_pk):
        question = get_object_or_404(Question, pk=question_pk)
        serializer = QuestionDetailSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, question_pk):
        question = get_object_or_404(Question, question_pk=question_pk)
        question.delete()
        messages = {
            'Delete': f"{question_pk}번 글이 삭제되었습니다."
        }
        return Response(messages, status=status.HTTP_204_NO_CONTENT)

class AnswerPutDeleteAPIView(APIView) :
    def get(self, request, answer_pk):
        answer = get_object_or_404(Answer, pk = answer_pk)
        serializer = AnswerSerializer(answer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, answer_pk):
        answer = get_object_or_404(Answer, pk = answer_pk)
        serializer = AnswerSerializer(answer, data = request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, answer_pk):
        answer = get_object_or_404(Answer, pk = answer_pk)
        answer.delete()
        messages = {
            'Delete' : f"{answer_pk}번 글이 삭제되었습니다."
        }
        return Response(messages, status=status.HTTP_204_NO_CONTENT)