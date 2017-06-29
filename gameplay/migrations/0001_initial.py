# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0018_messagecenter_deleted'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gameplay',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('amount', models.FloatField(max_length=15)),
                ('choice', models.CharField(max_length=5, choices=[(b'YES', b'YES'), (b'NO', b'NO')])),
                ('status', models.CharField(max_length=10, choices=[(b'OPEN', b'OPEN'), (b'CLOSED', b'CLOSED')])),
                ('decision', models.CharField(max_length=10, choices=[(b'WIN', b'WIN'), (b'LOST', b'LOST')])),
                ('amount_won', models.FloatField(default=0.0, max_length=15)),
                ('event', models.ForeignKey(blank=True, to='general.Event', null=True)),
                ('user', models.ForeignKey(blank=True, to='general.UserAccount', null=True)),
            ],
            options={
                'ordering': ['date'],
            },
        ),
    ]
