# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('basil', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(default=datetime.date.today)),
                ('description', models.CharField(max_length=200)),
                ('notes', models.CharField(max_length=100, null=True)),
                ('account', models.ForeignKey(to='basil.Account')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction_Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('fixed_cost', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='transaction',
            name='transaction_category',
            field=models.ForeignKey(to='basil.Transaction_Category'),
        ),
    ]
