# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('foodpantry', '0004_auto_20150412_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drives',
            name='last_tweeted',
            field=models.DateTimeField(default=datetime.datetime(1900, 4, 13, 3, 49, 58, 130683, tzinfo=utc), verbose_name=b'last tweet'),
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='last_tweeted',
            field=models.DateTimeField(default=datetime.datetime(1900, 4, 13, 3, 49, 58, 125033, tzinfo=utc), verbose_name=b'last tweet'),
        ),
    ]
