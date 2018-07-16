# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-15 08:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yezi_weibo', '0004_auto_20180618_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wbuser',
            name='_info',
            field=models.TextField(blank=True, null=True, verbose_name='其他信息'),
        ),
        migrations.AlterField(
            model_name='wbuser',
            name='nickname',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='昵称'),
        ),
    ]