# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0044_auto_20170912_0354'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='decided',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.TimeField(default=datetime.datetime(2017, 9, 12, 9, 55, 48, 851142, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.TimeField(default=datetime.datetime(2017, 9, 12, 9, 55, 48, 851105, tzinfo=utc)),
        ),
    ]
