from django.db import models
from django.utils.translation import gettext_lazy as _


class CategoryType(models.TextChoices) :
    # 언어 선택
    Python = 'Python', _('Python')
    Java = 'Java', _('Java')
    JavaScript = 'JavaScript', _('JavaScript')
    C = 'C', _('C')
    CCC = 'C++', _('C++')
    Flutter = 'Flutter', _('Flutter')
    Kotlin = 'Kotlin', _('Kotlin')
    Swift = 'Swift', _('Swift')
    Dart = 'Dart', _('Dart')
    PHP = 'PHP', _('PHP')
    TypeScript = 'TypeScript', _('TypeScript')
    Go = 'Go', _('Go')

    # SQL 선택
    MySQL = 'MySQL', _('MySQL')
    PostgreSQL = 'PostgreSQL', _('PostgreSQL')
    MariaDB = 'MariaDB', _('MariaDB')
    Oracle = 'Oracle', _('Oracle')
    MsSQL = 'MsSQL', _('MsSQL')

    # NoSQL 선택
    Redis = 'Redis', _('Redis')
    MongoDB = 'MongoDB', _('MongoDB')

    # 배포 환경
    CS = 'CS', _('CS')
    etc = 'etc', _('etc')


class Question(models.Model) :
    Question_title = models.CharField(max_length=100, verbose_name='질문 제목', null=False)
    Question_category1 = models.CharField(
        choices=CategoryType.choices,
        max_length=20,
        null=False,
    )
    Question_category2 = models.CharField(
        choices=CategoryType.choices,
        max_length=20,
        blank=True
    )
    Question_category3 = models.CharField(
        choices=CategoryType.choices,
        max_length=20,
        blank=True
    )
    Question_category4 = models.CharField(
        choices=CategoryType.choices,
        max_length=20,
        blank=True
    )
    Question_content = models.TextField(verbose_name='질문 내용', null=False)
    Question_image = models.ImageField(upload_to='uploads/%Y/%m/%d/', null=True, blank=True, verbose_name='질문 사진')
    Question_created_at = models.DateTimeField(auto_now_add=True, null=False, verbose_name='질문 날짜')
    Question_counting = models.IntegerField(default=0, verbose_name='질문 조회수')

    def __str__(self):
        return self.Question_title

    class Meta :
        db_table = 'Questions'


class Answer(models.Model) :
    question = models.ForeignKey(Question, related_name='answers' ,on_delete=models.CASCADE)
    Answer_title = models.CharField(max_length=100, verbose_name='답변 제목', null=False)
    Answer_content = models.TextField(verbose_name='답변 내용', null=False)
    Answer_image = models.ImageField(upload_to='uploads/%Y/%m/%d/', null=True, blank=True, verbose_name='답변 사진')
    Answer_created_at = models.DateTimeField(auto_now_add=True, null=False, verbose_name='답변 날짜')

    def __str__(self):
        return self.Answer_title

    class Meta :
        db_table = 'Answers'