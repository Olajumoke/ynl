# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0040_auto_20170819_0142'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='end_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='event',
            name='start_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.TimeField(default=datetime.datetime(2017, 9, 11, 14, 9, 22, 795292, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.TimeField(default=datetime.datetime(2017, 9, 11, 14, 9, 22, 795254, tzinfo=utc)),
        ),
    ]
