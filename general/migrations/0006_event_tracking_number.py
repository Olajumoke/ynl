# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0005_auto_20170611_2217'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='tracking_number',
            field=models.CharField(max_length=250, null=True, blank=True),
        ),
    ]
