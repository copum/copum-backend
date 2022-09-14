from collections import UserDict
from django.db import models
from users.models import User


class Posts(models.Model):
    post_name = models.CharField(max_length=100)
    post_content = models.CharField(max_length=300)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'writer',null=True) # 작성자 id
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)