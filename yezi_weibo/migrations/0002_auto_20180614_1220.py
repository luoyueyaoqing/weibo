# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-14 04:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yezi_weibo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wbtext',
            options={'verbose_name': '微博', 'verbose_name_plural': '微博'},
        ),
    ]