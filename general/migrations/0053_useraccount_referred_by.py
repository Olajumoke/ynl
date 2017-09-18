# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0052_remove_useraccount_referred_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='referred_by',
            field=models.ForeignKey(blank=True, to='general.Referral', null=True),
        ),
    ]
