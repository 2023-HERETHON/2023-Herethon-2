# Generated by Django 4.2.3 on 2023-07-11 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0003_alter_arm_health_arm_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='exer_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arm_name', models.CharField(max_length=20)),
                ('content', models.TextField(null=True)),
            ],
        ),
    ]
