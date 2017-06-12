# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0004_remove_event_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='closed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.CharField(blank=True, max_length=50, null=True, choices=[(b'', b'Select Category'), (b'SPORT', b'SPORT'), (b'BUSINESS', b'BUSINESS'), (b'FASHION', b'FASHION'), (b'POLITICS', b'POLITICS'), (b'ENTERTAINMENT', b'ENTERTAINMENT'), (b'EDUCATION', b'EDUCATION'), (b'SCIENCE&TECH', b'SCIENCE&TECH')]),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.DateField(null=True, blank=True),
        ),
    ]
