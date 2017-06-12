# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0002_auto_20170605_1253'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='gender',
            field=models.CharField(blank=True, max_length=10, null=True, choices=[(b'', b'Select Gender'), (b'FEMALE', b'FEMALE'), (b'MALE', b'MALE')]),
        ),
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.CharField(blank=True, max_length=50, null=True, choices=[(b'', b'Select Category'), (b'SPORT', b'SPORT'), (b'BUSINESS', b'BUSINESS'), (b'FASHION', b'FASHION'), (b'POLITICS', b'POLITICS'), (b'ENTERTAINMENT', b'ENTERTAINMENT'), (b'EDUCATION', b'EDUCATION'), (b'SCIENCE&TECH', b'SCIENCE&TECH')]),
        ),
    ]
