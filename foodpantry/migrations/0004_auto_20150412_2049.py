# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('foodpantry', '0003_auto_20150410_0327'),
    ]

    operations = [
        migrations.AddField(
            model_name='drives',
            name='address',
            field=models.CharField(default='no address found', max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='drives',
            name='last_tweeted',
            field=models.DateTimeField(default=datetime.datetime(1900, 4, 12, 20, 48, 34, 548162, tzinfo=utc), verbose_name=b'last tweet'),
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='last_tweeted',
            field=models.DateTimeField(default=datetime.datetime(1900, 4, 12, 20, 48, 34, 544031, tzinfo=utc), verbose_name=b'last tweet'),
        ),
    ]
