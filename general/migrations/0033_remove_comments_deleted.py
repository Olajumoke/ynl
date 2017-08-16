# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0032_comments_liked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='deleted',
        ),
    ]
