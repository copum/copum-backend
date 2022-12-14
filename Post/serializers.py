from rest_framework import serializers

from .models import Question, Answer, Category


class CategorySerializer(serializers.ModelSerializer) :
    class Meta :
        model = Category
        fields = ('id','category_name')


class AnswerSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Answer
        fields = ('question', 'Answer_title', 'Answer_content', 'Answer_image')


class QuestionSerializer(serializers.ModelSerializer) :
    answers_count = serializers.IntegerField(source='answers.count', read_only=True)

    class Meta :
        model = Question
        fields = ('pk', 'Question_category1', 'Question_category2', 'Question_category3', 'Question_category4', \
                  'Question_title', 'Question_content', 'Question_image','Question_counting', 'answers_count')


class QuestionDetailSerializer(serializers.ModelSerializer) :
    answers = AnswerSerializer(many=True , read_only=True)
    answers_count = serializers.IntegerField(source='answers.count', read_only= True)

    class Meta :
        model = Question
        fields  = ('Question_category1', 'Question_category2', 'Question_category3', 'Question_category4', \
                   'Question_title', 'Question_content','Question_image','Question_created_at', \
                   'Question_counting', 'answers_count', 'answers')
