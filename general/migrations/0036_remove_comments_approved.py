# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0035_remove_comments_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='approved',
        ),
    ]
