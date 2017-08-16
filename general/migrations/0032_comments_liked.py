# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0031_auto_20170813_1900'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='liked',
            field=models.BooleanField(default=False),
        ),
    ]
