from django.db import models
import datetime

class Account_Type(models.Model):
    account_type = models.CharField(max_length=200)


class Account(models.Model):
    account_type = models.ForeignKey(Account_Type)
    name = models.CharField(max_length=200)

class Transaction_Category(models.Model):
    name = models.CharField(max_length=200)
    fixed_cost = models.BooleanField(default=False)


class Payee(models.Model):
    name = models.CharField(max_length=200)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }

class Transaction(models.Model):
    transaction_category = models.ForeignKey(Transaction_Category, null=True)
    account = models.ForeignKey(Account)
    date = models.DateField(default=datetime.date.today)
    description = models.CharField(max_length=200)
    place = models.ForeignKey(Payee, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.CharField(max_length=100, null=True)

