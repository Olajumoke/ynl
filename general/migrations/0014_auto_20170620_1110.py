# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0013_messagecentercomment_image_obj'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagecenter',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='messagecentercomment',
            name='message_obj',
            field=models.ForeignKey(blank=True, to='general.MessageCenter', null=True),
        ),
        migrations.AlterField(
            model_name='messagecentercomment',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
