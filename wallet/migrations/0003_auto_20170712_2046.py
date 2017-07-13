# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0002_auto_20170628_0009'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='betpayments',
            options={'ordering': ['-date']},
        ),
    ]
