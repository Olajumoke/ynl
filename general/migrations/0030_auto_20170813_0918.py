# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0029_comments_deleted'),
    ]

    operations = [
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('like', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['-created_on'],
                'verbose_name_plural': 'Likes',
            },
        ),
        migrations.AlterField(
            model_name='comments',
            name='approved',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='likes',
            name='comment_obj',
            field=models.ForeignKey(blank=True, to='general.Comments', null=True),
        ),
    ]
