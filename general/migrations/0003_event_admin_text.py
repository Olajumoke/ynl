# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
# import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0002_auto_20170605_1253'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='admin_text',
            field=models.TextField(null=True, blank=True),
        ),
    ]
