# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0047_auto_20170915_1343'),
    ]

    operations = [
        migrations.CreateModel(
            name='Referral',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('referrer', models.ForeignKey(blank=True, to='general.UserAccount', null=True)),
            ],
            options={
                'verbose_name_plural': 'Refferer',
            },
        ),
    ]
