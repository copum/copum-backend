from collections import UserDict
from django.db import models
from users.models import User
from django.utils.translation import gettext_lazy as _


class Posts(models.Model):
    post_name = models.CharField(max_length=100)
    post_content = models.CharField(max_length=300)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'writer',null=True) # 작성자 id
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CategoryType(models.TextChoices):
    # 언어 선택
    Python = 'Python', _('Python')
    Java = 'Java', _('Java')
    JavaScript = 'JavaScript', _('JavaScript')
    C = 'C', _('C')
    CCC = 'C++', _('C++')
    Flutter = 'Flutter', _('Flutter')
    Kotlin = 'Kotiln', _('Kotiln')
    Swift = 'Swift', _('Swift')
    Dart = 'Dart', _('Dart')
    PHP = 'PHP', _('PHP')
    TypeScript = 'TypeScript', _('TypeScript')
    Go = 'Go', _('Go')

    # SQL 선택
    MySQL = 'MySQL', _('MySQL')
    PostgreSQL = 'PostgreSQL', _('PostgreSQL')
    MariaDB = 'MariaDB', _('MAriaDB')
    Oracle = 'Oracle', _('Oracle')
    MsSQL = 'MsSQL', _('MsSQL')

    # NoSQL 선택
    Redis = 'Redis', _('Redis')
    MongoDB = 'MongoDB', _('MongoDB')

    # Container
    Docker = 'Docker', _('Docker')
    Kubernetes = 'Kubernetes', _('Kubernetes')

    # 배포 환경
    Heroku = 'Heroku', _('Heroku')
    AWS = 'AWS', _('AWS')
    # CS
    CS = 'CS', _('CS')
    # 기타..등
    etc = 'etc', _('etc')


class Question(models.Model):
    title = models.CharField(max_length=100, verbose_name='질문 제목', null=False, blank=False)
    category = models.CharField(
        choices=CategoryType.choices,
        max_length=20,
        default=CategoryType.etc
    )
    content = models.TextField(verbose_name='질문 내용', null=False, Blank=False)
    codes = models.TextField(verbose_name='질문 코드', null=True, Blank=True)
    image = models.ImageField(upload_to='uploads/%Y/%m/%d/', null=True, blank=True, verbose_name='질문 사진')
    created_at = models.DateTimeField(auto_now_add=True, null=False, verbose_name='질문 날짜')
    updated_at = models.DateTimeField(auto_now_add=True, null=False, verbose_name='질문 수정 날짜')

    def __str__(self):
        return self.Question_title

    class Meta :
        db_table = 'Questions'


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name='답변 제목', blank=False, null=False)
    content = models.TextField(verbose_name='답변 내용', null=False, blank=False)
    codes = models.TextField(verbose_name='답변 코드', null=True, blank=False)
    image = models.ImageField(upload_to='uploads/%Y/%m/%d/', null=True, verbose_name='답변 사진', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False, verbose_name='답변 날짜')
    updated_at = models.DateTimeField(auto_now_add=True, null=False, verbose_name='질문 수정 날짜')

    class Meta :
        db_table = 'Answers'