# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DateUploaded',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(default=datetime.datetime(2015, 4, 10, 3, 16, 36, 932179, tzinfo=utc), verbose_name=b'date published')),
            ],
        ),
        migrations.CreateModel(
            name='FoodDrives',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('start_date', models.DateTimeField(verbose_name=b'Drive Date')),
                ('duration', models.IntegerField(default=0)),
                ('notes', models.CharField(max_length=200)),
                ('last_tweeted', models.DateTimeField(default=datetime.datetime(2015, 4, 10, 3, 16, 36, 937691, tzinfo=utc), verbose_name=b'last tweet')),
                ('created_on', models.DateTimeField(default=datetime.datetime(2015, 4, 10, 3, 16, 36, 937720, tzinfo=utc), verbose_name=b'date published')),
            ],
        ),
        migrations.CreateModel(
            name='FoodGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('optimal_number', models.IntegerField(default=0)),
                ('current_number', models.IntegerField(default=0)),
                ('change', models.IntegerField(default=0)),
                ('deficit', models.IntegerField(default=0)),
                ('upload_date', models.ForeignKey(to='foodpantry.DateUploaded')),
            ],
        ),
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('optimal_number', models.IntegerField(default=0)),
                ('current_number', models.IntegerField(default=0)),
                ('change', models.IntegerField(default=0)),
                ('deficit', models.IntegerField(default=0)),
                ('priority', models.CharField(default=b'low', max_length=200)),
                ('last_tweeted', models.DateTimeField(default=datetime.datetime(2015, 4, 10, 3, 16, 36, 933941, tzinfo=utc), verbose_name=b'last tweet')),
                ('food_group', models.ForeignKey(to='foodpantry.FoodGroup')),
                ('upload_date', models.ForeignKey(to='foodpantry.DateUploaded')),
            ],
        ),
        migrations.CreateModel(
            name='Frequency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number_of_days', models.IntegerField(default=0)),
                ('category', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PastTweets',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tweet', models.CharField(max_length=140)),
                ('date', models.DateTimeField(default=datetime.datetime(2015, 4, 10, 3, 16, 36, 936971, tzinfo=utc), verbose_name=b'date published')),
            ],
        ),
        migrations.CreateModel(
            name='TweetOptions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('upload_date', models.DateTimeField(default=datetime.datetime(2015, 4, 10, 3, 16, 36, 935967, tzinfo=utc), verbose_name=b'date published')),
                ('tweet', models.CharField(max_length=140)),
                ('category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tweets',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tweet', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='TweetSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('upload_date', models.DateTimeField(default=datetime.datetime(2015, 4, 10, 3, 16, 36, 934721, tzinfo=utc), verbose_name=b'date published')),
                ('deficit_hp', models.IntegerField(default=0)),
                ('deficit_np', models.IntegerField(default=0)),
                ('deficit_lp', models.IntegerField(default=0)),
                ('max_per_day', models.IntegerField(default=0)),
                ('change_for_thanks', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='frequency',
            name='settings',
            field=models.ForeignKey(to='foodpantry.TweetSettings'),
        ),
    ]
