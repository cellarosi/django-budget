import datetime
from decimal import Decimal
from django.db import models
from budget.categories.models import Category, StandardMetadata, ActiveManager


TRANSACTION_TYPES = (
    ('debit', 'Debit'),
    ('credit', 'Credit'),
)


class TransactionManager(ActiveManager):
    pass


class Transaction(StandardMetadata):
    transaction_type = models.CharField(max_length=32, choices=TRANSACTION_TYPES, default='debit', db_index=True)
    name = models.CharField(max_length=255, blank=True)
    category = models.ForeignKey(Category)
    amount = models.DecimalField(max_digits=11, decimal_places=2)
    date = models.DateField(default=datetime.date.today, db_index=True)
    
    objects = models.Manager()
    active = ActiveManager()
    # debits = TransactionDebitManager()
    # credits = TransactionCreditManager()
    
    def __unicode__(self):
        return u"%s (%s) - %s" % (self.name, self.get_transaction_type_display(), self.amount)
    