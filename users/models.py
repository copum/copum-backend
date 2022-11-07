from django.db import models


class User(models.Model):
    LOGIN_TYPE = [
        ('KAKAO', 'kakao'),
        ('GOOGLE', 'google'),
        ('NAVER', 'naver'),
    ]
    user_id = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    nickname = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    login_type= models.CharField(blank=True, max_length=255, choices=LOGIN_TYPE)

    class Meta:
        db_table = 'users'

class Profile(models.Model) :
    user = models.Foreignkey(User, related_name='User', on_delete = models.Cascade)