# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0049_auto_20170917_1037'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='total_amt',
            field=models.FloatField(default=0.0, max_length=15),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.TimeField(default=datetime.datetime(2017, 9, 17, 22, 9, 50, 454283, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.TimeField(default=datetime.datetime(2017, 9, 17, 22, 9, 50, 454251, tzinfo=utc)),
        ),
    ]
