# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-21 04:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20160921_1422'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='name',
        ),
        migrations.AddField(
            model_name='author',
            name='first_name',
            field=models.CharField(default='Ben', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='author',
            name='last_name',
            field=models.CharField(default='Bova', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(
                help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>', max_length=13),
        ),
        migrations.AlterField(
            model_name='book',
            name='subject',
            field=models.ManyToManyField(
                help_text='Select a grouping category for this book', to='catalog.Subject', verbose_name='Category'),
        ),
    ]
