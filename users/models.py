from django.db import models


class User(models.Model):
    LOGIN_TYPE = [
        ('KAKAO', 'kakao'),
        ('GOOGLE', 'google'),
        ('NAVER', 'naver'),
    ]
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=255)
    login_type= models.CharField(blank=True, max_length=255, choices=LOGIN_TYPE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'users'

