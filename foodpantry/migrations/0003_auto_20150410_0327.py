# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodpantry', '0002_auto_20150410_0317'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FoodDrives',
            new_name='Drives',
        ),
    ]
