# Generated by Django 4.1.2 on 2023-01-05 19:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("Post", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="question",
            name="Author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="question",
            name="Question_category1",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="카테고리1",
                to="Post.category",
            ),
        ),
        migrations.AddField(
            model_name="question",
            name="Question_category2",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="카테고리2",
                to="Post.category",
            ),
        ),
        migrations.AddField(
            model_name="question",
            name="Question_category3",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="카테고리3",
                to="Post.category",
            ),
        ),
        migrations.AddField(
            model_name="question",
            name="Question_category4",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="카테고리4",
                to="Post.category",
            ),
        ),
        migrations.AddField(
            model_name="answer",
            name="Author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="answer",
            name="question",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="answers",
                to="Post.question",
            ),
        ),
    ]