# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0023_replies'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]
