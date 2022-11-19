from django.db import models


class User(models.Model):
    LOGIN_TYPE = [
        ('KAKAO', 'kakao'),
        ('GOOGLE', 'google'),
        ('NAVER', 'naver'),
    ]
    user_id = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='profile_images', blank=True, null=True, verbose_name='프로필 사진')
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=255, null=True)
    login_type= models.CharField(blank=True, max_length=255, choices=LOGIN_TYPE)

    class Meta:
        db_table = 'users'

