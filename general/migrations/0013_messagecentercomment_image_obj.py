# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0012_messagecenter_messagecentercomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='messagecentercomment',
            name='image_obj',
            field=models.ImageField(null=True, upload_to='image_obj', blank=True),
        ),
    ]
