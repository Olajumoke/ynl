# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0043_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='validated',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.TimeField(default=datetime.datetime(2017, 9, 12, 2, 54, 11, 369608, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.TimeField(default=datetime.datetime(2017, 9, 12, 2, 54, 11, 369573, tzinfo=utc)),
        ),
    ]
