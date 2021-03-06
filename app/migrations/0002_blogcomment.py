# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-05 09:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100, verbose_name='评论者名字')),
                ('user_email', models.EmailField(max_length=255, verbose_name='评论者邮箱')),
                ('body', models.TextField(verbose_name='评论内容')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='评论发表时间')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Article', verbose_name='评论所属文章')),
            ],
        ),
    ]
