from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from .models import Posts, Question

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ('post_name','post_content',)


# ------------------------------------------------------------

