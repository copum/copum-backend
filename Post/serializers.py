from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from .models import Posts, Question

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ('post_name','post_content',)


# ------------------------------------------------------------
class QuestionListSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Question
        fields = ('Question_id', 'Question_title', 'Question_created_at', 'Question_view_count')


class QuestionCreateSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Question
        fields = ('Question_category', 'Question_title', 'Question_content', 'Question_codes', \
                'Question_image' )


class QuestionSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Question
        fields = '__all__'