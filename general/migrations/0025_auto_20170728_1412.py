# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0024_comments_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='approve',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.CharField(blank=True, max_length=50, null=True, choices=[(b'', b'Select Category'), (b'SPORT', b'SPORT'), (b'BUSINESS', b'BUSINESS'), (b'FASHION', b'FASHION'), (b'POLITICS', b'POLITICS'), (b'ENTERTAINMENT', b'ENTERTAINMENT'), (b'EDUCATION', b'EDUCATION'), (b'STEM', b'STEM')]),
        ),
    ]
