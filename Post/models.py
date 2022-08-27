from django.db import models


class Posts(models.Model):
    post_name = models.CharField(max_length=100)
    post_content = models.CharField(max_length=300)