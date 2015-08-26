# Aysin Oruz
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShortUrl',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField(max_length=500, verbose_name=b'Url')),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'Datetime')),
            ],
            options={
                'ordering': ['datetime'],
            },
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name=b'title')),
            ],
        ),
        migrations.AddField(
            model_name='shorturl',
            name='word',
            field=models.OneToOneField(related_name='word_urls', to='projects.Word'),
        ),
    ]