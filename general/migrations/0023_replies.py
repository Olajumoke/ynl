# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0022_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='Replies',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reply', models.TextField()),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('name', models.CharField(max_length=150, null=True, blank=True)),
                ('email', models.CharField(max_length=150, null=True, blank=True)),
                ('comment_obj', models.ForeignKey(blank=True, to='general.Comments', null=True)),
            ],
            options={
                'ordering': ['-created_on'],
                'verbose_name_plural': 'Responses',
            },
        ),
    ]
