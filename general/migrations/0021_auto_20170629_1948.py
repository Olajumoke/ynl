# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0020_auto_20170629_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='bet_question',
            field=models.CharField(max_length=250, null=True, blank=True),
        ),
    ]
