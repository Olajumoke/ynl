# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0046_auto_20170913_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.CharField(blank=True, max_length=50, null=True, choices=[(b'', b'Select Category'), (b'Sports', b'Sports'), (b'Entertainment-LifeStyle', b'Entertainment & LifeStyle'), (b'General', b'General'), (b'Politics', b'Politics'), (b'Business-Economy', b'Business & Economy')]),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.TimeField(default=datetime.datetime(2017, 9, 16, 15, 27, 10, 478710, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.TimeField(default=datetime.datetime(2017, 9, 16, 15, 27, 10, 478672, tzinfo=utc)),
        ),
    ]
