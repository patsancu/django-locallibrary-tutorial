# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-21 05:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_auto_20160921_1444'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False,
                 help_text='Unique ID for this particular book across whole library', primary_key=True, serialize=False)),
                ('summary', models.TextField(
                    help_text='Enter a brief description of the book', max_length=1000)),
                ('imprint', models.CharField(max_length=200)),
                ('due_back', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('d', 'maintenance'), ('o', 'on loan'), (
                    'a', 'available'), ('r', 'reserved')], default='d', help_text='Book availability', max_length=1)),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='imprint',
        ),
        migrations.AlterField(
            model_name='author',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bookinstance',
            name='book',
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Book'),
        ),
    ]
