# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basil', '0002_auto_20150521_0139'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='place',
            field=models.ForeignKey(to='basil.Payee', null=True),
        ),
    ]
