# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0019_auto_20170629_1234'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_decision',
            field=models.CharField(blank=True, max_length=5, null=True, choices=[(b'YES', b'YES'), (b'NO', b'NO')]),
        ),
    ]
