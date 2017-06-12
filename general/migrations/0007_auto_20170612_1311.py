# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0006_event_tracking_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='tracking_number',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
