# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basil', '0004_auto_20150521_0157'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AccountType',
            new_name='Account_Type',
        ),
    ]
