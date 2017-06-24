# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0017_auto_20170621_0845'),
    ]

    operations = [
        migrations.AddField(
            model_name='messagecenter',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]
