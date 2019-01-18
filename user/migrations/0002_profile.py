# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-01-18 01:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dating_sex', models.CharField(choices=[('male', '男'), ('female', '女')], default='female', max_length=16, verbose_name='匹配的性别')),
                ('location', models.CharField(max_length=32, verbose_name='目标城市')),
                ('min_distance', models.IntegerField(default=1, verbose_name='最小交友距离')),
                ('max_distance', models.IntegerField(default=100, verbose_name='最大交友距离')),
                ('min_dating_age', models.IntegerField(default=18, verbose_name='最小交友年龄')),
                ('max_dating_age', models.IntegerField(default=80, verbose_name='最大交友年龄')),
                ('vibration', models.BooleanField(default=True, verbose_name='是否开启震动')),
                ('only_match', models.BooleanField(default=False, verbose_name='不让匹配的人看到我的相册')),
                ('auto_play', models.BooleanField(default=True, verbose_name='是否自动播放')),
            ],
        ),
    ]
