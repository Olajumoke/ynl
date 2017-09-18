# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0051_auto_20170918_0934'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='referred_by',
        ),
    ]
