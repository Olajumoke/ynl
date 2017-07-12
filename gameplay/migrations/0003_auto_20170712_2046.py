# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameplay', '0002_auto_20170629_0152'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gameplay',
            options={'ordering': ['-date']},
        ),
    ]
