# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('foodpantry', '0006_auto_20150414_0325'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweetsettings',
            name='freq_hp',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tweetsettings',
            name='freq_lp',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tweetsettings',
            name='freq_np',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='drives',
            name='last_tweeted',
            field=models.DateTimeField(default=datetime.datetime(1900, 4, 14, 3, 48, 32, 653795, tzinfo=utc), verbose_name=b'last tweet'),
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='last_tweeted',
            field=models.DateTimeField(default=datetime.datetime(1900, 4, 14, 3, 48, 32, 648068, tzinfo=utc), verbose_name=b'last tweet'),
        ),
    ]
