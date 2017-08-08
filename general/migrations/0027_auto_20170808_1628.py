# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0026_auto_20170728_1432'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='approved',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='deleted',
        ),
        migrations.AlterField(
            model_name='comments',
            name='text',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='comments',
            name='username',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
