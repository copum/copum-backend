from django.db import models

from users.model import User


class Category(models.Model) :
    category_name = models.CharField(max_length=20, verbose_name='카테고리 명')

    def __str__(self):
        return self.category_name

    class Meta :
        db_table = 'Categories'


def question_image_rename(instance, filename):
    ext = filename.split('.')[-1]
    return f'question/question_{instance.pk}/image{filename[0]}.{ext}'


class Question(models.Model) :
    Question_title = models.CharField(max_length=100, verbose_name='질문 제목', null=False)
    Question_category1 = models.ForeignKey(Category, related_name='카테고리1', on_delete=models.CASCADE)
    Question_category2 = models.ForeignKey(Category, related_name='카테고리2', blank=True, null=True,
                                           on_delete=models.CASCADE)
    Question_category3 = models.ForeignKey(Category, related_name='카테고리3', blank=True, null=True,
                                           on_delete=models.CASCADE)
    Question_category4 = models.ForeignKey(Category, related_name='카테고리4', blank=True, null=True,
                                           on_delete=models.CASCADE)
    Question_content = models.TextField(verbose_name='질문 내용', null=False)
    Question_image = models.ImageField(upload_to=question_image_rename, null=True, blank=True, verbose_name='질문 사진')
    Question_created_at = models.DateTimeField(auto_now_add=True, null=False, verbose_name='질문 날짜')
    Question_counting = models.IntegerField(default=0, verbose_name='질문 조회수')
    # Question_Empathy = models.ManyToManyField(User)

    def __str__(self):
        return self.Question_title

    class Meta :
        db_table = 'Questions'


def answer_image_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance :
        return f'answer/answer_{instance.pk}/image{filename[0]}.{ext}'
    else :
        return f'answer/image{filename[0]}.{ext}'


class Answer(models.Model) :
    question = models.ForeignKey(Question, related_name='answers' ,on_delete=models.CASCADE)
    Answer_title = models.CharField(max_length=100, verbose_name='답변 제목', null=False)
    Answer_content = models.TextField(verbose_name='답변 내용', null=False)
    Answer_image = models.ImageField(upload_to=answer_image_rename, null=True, blank=True, verbose_name='답변 사진')
    Answer_created_at = models.DateTimeField(auto_now_add=True, null=False, verbose_name='답변 날짜')

    def __str__(self):
        return self.Answer_title

    class Meta :
        db_table = 'Answers'