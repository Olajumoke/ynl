# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0018_messagecenter_deleted'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='tracking_number',
            new_name='bet_question',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='large_event_image',
            new_name='event_image',
        ),
        migrations.RemoveField(
            model_name='event',
            name='admin_text',
        ),
        migrations.RemoveField(
            model_name='event',
            name='medium_event_image',
        ),
        migrations.RemoveField(
            model_name='event',
            name='small_event_image',
        ),
        migrations.AddField(
            model_name='event',
            name='event_id',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='event',
            name='event_msg_body',
            field=models.TextField(null=True, blank=True),
        ),
    ]
