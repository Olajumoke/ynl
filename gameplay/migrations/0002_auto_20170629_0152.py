# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameplay', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameplay',
            name='amount_won',
            field=models.FloatField(default=0.0, max_length=15, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='gameplay',
            name='choice',
            field=models.CharField(blank=True, max_length=5, null=True, choices=[(b'YES', b'YES'), (b'NO', b'NO')]),
        ),
        migrations.AlterField(
            model_name='gameplay',
            name='decision',
            field=models.CharField(blank=True, max_length=10, null=True, choices=[(b'WIN', b'WIN'), (b'LOST', b'LOST')]),
        ),
        migrations.AlterField(
            model_name='gameplay',
            name='status',
            field=models.CharField(blank=True, max_length=10, null=True, choices=[(b'OPEN', b'OPEN'), (b'CLOSED', b'CLOSED')]),
        ),
    ]
