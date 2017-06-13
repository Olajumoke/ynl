# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0010_useraccount_deleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='bank',
            field=models.CharField(blank=True, max_length=100, null=True, choices=[(b'', b'Select Bank'), (b'ACCESS BANK', b'ACCESS BANK'), (b'CITIBANK', b'CITIBANK'), (b'DIAMOND BANK', b'DIAMOND BANK'), (b'ECOBANK', b'ECOBANK'), (b'FIDELITY BANK', b'FIDELITY BANK'), (b'FIRST CITY MONUMENT BANK', b'FIRST CITY MONUMENT BANK'), (b'FIRST BANK', b'FIRST BANK'), (b'GUARANTY TRUST BANK', b'GUARANTY TRUST BANK'), (b'HERITAGE BANK', b'HERITAGE BANK'), (b'KEYSTONE BANK', b'KEYSTONE BANK'), (b'SKYE BANK', b'SKYE BANK'), (b'STANBIC IBTC', b'STANBIC IBTC'), (b'STANDARD CHARTERED BANK', b'STANDARD CHARTERED BANK'), (b'STERLING BANK', b'STERLING BANK'), (b'UNION BANK OF NIGERIA', b'UNION BANK OF NIGERIA'), (b'UNITED BANK OF AFRICA', b'UNITED BANK OF AFRICA'), (b'UNITY BANK', b'UNITY BANK'), (b'WEMA BANK', b'WEMA BANK'), (b'ZENITH BANK', b'ZENITH BANK')]),
        ),
    ]
