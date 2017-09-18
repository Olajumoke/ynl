# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0048_referral'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='profile_updated',
            field=models.BooleanField(default=False),
        ),
    ]
