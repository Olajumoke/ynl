# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0025_auto_20170728_1412'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='approve',
            new_name='approved',
        ),
        migrations.AlterField(
            model_name='comments',
            name='text',
            field=models.CharField(max_length=2000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='comments',
            name='username',
            field=models.CharField(max_length=150, null=True, blank=True),
        ),
    ]
