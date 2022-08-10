# Generated by Django 4.0.6 on 2022-08-10 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=255)),
                ('login_type', models.CharField(blank=True, choices=[('KAKAO', 'kakao'), ('GOOGLE', 'google'), ('NAVER', 'naver')], max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
