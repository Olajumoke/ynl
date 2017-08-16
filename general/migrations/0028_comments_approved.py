# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0027_auto_20170808_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
