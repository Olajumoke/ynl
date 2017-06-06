# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=50, null=True, blank=True)),
                ('text', models.CharField(max_length=1000, null=True, blank=True)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('email', models.EmailField(max_length=254, null=True, blank=True)),
            ],
            options={
                'ordering': ['-created_on'],
                'verbose_name_plural': 'Comment',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250, null=True, blank=True)),
                ('category', models.CharField(blank=True, max_length=50, null=True, choices=[(b'', b'Select country'), (b'SPORT', b'SPORT'), (b'BUSINESS', b'BUSINESS'), (b'FASHION', b'FASHION'), (b'POLITICS', b'POLITICS'), (b'ENTERTAINMENT', b'ENTERTAINMENT'), (b'EDUCATION', b'EDUCATION'), (b'SCIENCE&TECH', b'SCIENCE&TECH')])),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('start_time', models.DateTimeField(null=True, blank=True)),
                ('end_time', models.DateTimeField(null=True, blank=True)),
                ('publish', models.BooleanField(default=False)),
                ('event_image', models.ImageField(null=True, upload_to='media/event/%Y/%M/%d/', blank=True)),
                ('author', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ['-created_on'],
                'verbose_name_plural': 'Event',
            },
        ),
        migrations.AddField(
            model_name='useraccount',
            name='user_image',
            field=models.ImageField(null=True, upload_to='media/user_image/%Y/%M/%d/', blank=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='bank',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='comments',
            name='event',
            field=models.ForeignKey(blank=True, to='general.Event', null=True),
        ),
    ]
