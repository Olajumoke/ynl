# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0045_auto_20170912_1055'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='published_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.CharField(blank=True, max_length=50, null=True, choices=[(b'', b'Select Category'), (b'Sports', b'Sports'), (b'Entertainment & LifeStyle', b'Entertainment & LifeStyle'), (b'General', b'General'), (b'Politics', b'Politics'), (b'Business & Economy', b'Business & Economy')]),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.TimeField(default=datetime.datetime(2017, 9, 13, 13, 22, 21, 75122, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.TimeField(default=datetime.datetime(2017, 9, 13, 13, 22, 21, 75086, tzinfo=utc)),
        ),
    ]
