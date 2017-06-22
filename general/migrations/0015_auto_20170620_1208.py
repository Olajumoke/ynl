# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0014_auto_20170620_1110'),
    ]

    operations = [
        migrations.AddField(
            model_name='messagecenter',
            name='subject',
            field=models.CharField(max_length=150, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='messagecenter',
            name='replied_on',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
