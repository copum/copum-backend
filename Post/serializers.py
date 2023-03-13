from rest_framework import serializers

from .models import Question, Answer, Category
from users.serializers import UserSerializer


from users.models import User



class CategorySerializer(serializers.ModelSerializer) :
    class Meta :
        model = Category
        fields = ('id','category_name')


class AnswerSerializer(serializers.ModelSerializer) :
    user = UserSerializer(many=True, read_only = True)
    class Meta :
        model = Answer
        fields = ('user','question', 'Answer_title', 'Answer_content','Answer_image','Author')

class UserDetailSerializer(serializers.ModelSerializer) :
  class Meta :
    model = User
    fields = ("pk", "email", "user_id", "profile_image")

class QuestionSerializer(serializers.ModelSerializer) :
    answers_count = serializers.IntegerField(source='answers.count', read_only=True)
    user = UserDetailSerializer(read_only = True)
    class Meta :
        model = Question 
        fields = ('user','pk', 'Question_category1', 'Question_category2', 'Question_category3', 'Question_category4', \
                  'Question_title', 'Question_content', 'Question_image','Question_counting', 'answers_count', 'Author','Question_created_at')


class QuestionDetailSerializer(serializers.ModelSerializer) :
    answers = AnswerSerializer(many=True , read_only=True)
    answers_count = serializers.IntegerField(source='answers.count', read_only= True)

    class Meta :
        model = Question
        fields  = ('Question_category1', 'Question_category2', 'Question_category3', 'Question_category4', \
                   'Question_title', 'Question_content','Question_image','Question_created_at', \
                   'Question_counting', 'answers_count', 'answers','Author')
