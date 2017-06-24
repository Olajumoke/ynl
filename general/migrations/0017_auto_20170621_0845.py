# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0016_auto_20170621_0312'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='messagecenter',
            options={'verbose_name_plural': 'Messages'},
        ),
        migrations.AlterModelOptions(
            name='messagecentercomment',
            options={'verbose_name_plural': 'Message Center Comments'},
        ),
    ]
