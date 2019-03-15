# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-02-19 12:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detail',
            name='Date',
        ),
        migrations.RemoveField(
            model_name='detail',
            name='Review',
        ),
        migrations.RemoveField(
            model_name='detail',
            name='Tag',
        ),
        migrations.AddField(
            model_name='detail',
            name='Date_str',
            field=models.CharField(default='2019-2-19', max_length=64),
        ),
        migrations.AlterField(
            model_name='detail',
            name='Asin_detail',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='detail',
            name='Asin_tag',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='detail',
            name='Review_content',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='detail',
            name='Reviewer',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='detail',
            name='Stars',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='detail',
            name='Title',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='detail',
            name='Total_reviews_detail',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='detail',
            name='Total_score_detail',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='product',
            name='Asin',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='product',
            name='Total_reviews',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='product',
            name='Total_score',
            field=models.CharField(max_length=64),
        ),
    ]