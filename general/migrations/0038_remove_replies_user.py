# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0037_auto_20170814_0724'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='replies',
            name='user',
        ),
    ]
