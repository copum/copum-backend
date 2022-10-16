from rest_framework import serializers
from .models import *


# ------------------------------------------------------------
class AnswerSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Answer
        fields = ('question', 'Answer_title', 'Answer_content', 'Answer_image')


class QuestionSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Question
        fields = ('Question_category', 'Question_title', 'Question_content', \
                  'Question_image')


class QuestionDetailSerializer(serializers.ModelSerializer) :
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta :
        model = Question
        fields = ('Question_category', 'Question_title', 'Question_content', \
                  'Question_image', 'Question_created_at''answers')