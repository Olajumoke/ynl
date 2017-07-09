# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0019_auto_20170629_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_msg_body',
            field=tinymce.models.HTMLField(null=True, blank=True),
        ),
    ]
