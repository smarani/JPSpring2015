# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('foodpantry', '0005_auto_20150413_0349'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodgroup',
            name='priority',
            field=models.CharField(default=b' ', max_length=100),
        ),
        migrations.AlterField(
            model_name='drives',
            name='last_tweeted',
            field=models.DateTimeField(default=datetime.datetime(1900, 4, 14, 3, 25, 55, 131367, tzinfo=utc), verbose_name=b'last tweet'),
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='last_tweeted',
            field=models.DateTimeField(default=datetime.datetime(1900, 4, 14, 3, 25, 55, 127358, tzinfo=utc), verbose_name=b'last tweet'),
        ),
    ]
