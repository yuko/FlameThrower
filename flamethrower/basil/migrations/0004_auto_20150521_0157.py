# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basil', '0003_transaction_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='amount',
            field=models.DecimalField(default=0.0, max_digits=10, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_category',
            field=models.ForeignKey(to='basil.Transaction_Category', null=True),
        ),
    ]
