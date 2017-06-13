# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0008_merge'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='event_image',
            new_name='large_event_image',
        ),
        migrations.AddField(
            model_name='event',
            name='medium_event_image',
            field=models.ImageField(null=True, upload_to='media/event/%Y/%M/%d/', blank=True),
        ),
        migrations.AddField(
            model_name='event',
            name='small_event_image',
            field=models.ImageField(null=True, upload_to='media/event/%Y/%M/%d/', blank=True),
        ),
    ]
