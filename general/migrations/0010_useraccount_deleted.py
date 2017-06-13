# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0009_auto_20170613_0752'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]
