# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0040_auto_20170819_0142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_msg_body',
            field=models.CharField(max_length=3500, null=True, blank=True),
        ),
    ]
