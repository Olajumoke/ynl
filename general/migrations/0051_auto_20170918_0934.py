# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0050_auto_20170918_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referral',
            name='referrer',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='referred_by',
            field=models.ForeignKey(blank=True, to='general.Referral', null=True),
        ),
    ]
