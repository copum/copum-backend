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
        # 글쓴이 경우 count 제외
        if request.user:
            question.Question_counting += 0
        # 글쓴이를 제외한 사람은 count
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


# class Question_Empathy(APIView) :
#     def get(self, request, question_pk):
#         question = get_object_or_404(Question, pk=question_pk)
#         # 공감 안에 요청을 보낼 유저가 있을 경우
#         if request.user in question.Question_.all() :
#             # QUESTION MODEL Empathy 추가한 후 로직
#             question.empathy.remove(request.user)
#             messages = {
#                 'Delete' : '공감 취소'
#             }
#         # 공감 안에 요청을 보낼 유저가 없을 경우
#         else :
#             question.empathy.add(request.user)
#             messages = {
#                 'Add' : '공감'
#             }
#         return Response(messages, status=status.HTTP_200_OK)