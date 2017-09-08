# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0039_auto_20170814_0732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_msg_body',
            field=models.TextField(null=True, blank=True),
        ),
    ]
