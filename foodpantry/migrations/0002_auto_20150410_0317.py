# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('foodpantry', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dateuploaded',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'date published'),
        ),
        migrations.AlterField(
            model_name='fooddrives',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'date published'),
        ),
        migrations.AlterField(
            model_name='fooddrives',
            name='last_tweeted',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'last tweet'),
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='last_tweeted',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'last tweet'),
        ),
        migrations.AlterField(
            model_name='pasttweets',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'date published'),
        ),
        migrations.AlterField(
            model_name='tweetoptions',
            name='upload_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'date published'),
        ),
        migrations.AlterField(
            model_name='tweetsettings',
            name='upload_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'date published'),
        ),
    ]
