# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0036_remove_comments_approved'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='deleted',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='liked',
        ),
    ]
