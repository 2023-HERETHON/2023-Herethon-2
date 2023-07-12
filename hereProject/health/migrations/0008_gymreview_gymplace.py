# Generated by Django 4.2.3 on 2023-07-12 14:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('health', '0007_gym_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='gymReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='제목')),
                ('body', models.TextField(default='', verbose_name='내용')),
            ],
        ),
        migrations.CreateModel(
            name='gymPlace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placeName', models.CharField(max_length=128, verbose_name='이름')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='등록일')),
                ('likes', models.ManyToManyField(blank=True, related_name='liked_gyms', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
