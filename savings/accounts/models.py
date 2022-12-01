from django.db import models
from django.conf import settings


class Source(models.Model):
    label = models.CharField(max_length=25)

    def __str__(self):
        return self.label


class Account(models.Model):
    TFSA = 'tfsa'
    RRSP = 'rrsp'
    UNREGISTERED = 'unregistered'

    ACCOUNT_TYPES = (
        (TFSA, 'TFSA'),
        (RRSP, 'RRSP'),
        (UNREGISTERED, 'Unregistered'),
    )

    source = models.ForeignKey(
        'accounts.Source',
        on_delete=models.SET_NULL,
        related_name='accounts',
        null=True,
        blank=False
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='accounts',
    )
    label = models.CharField(max_length=25)
    account_type = models.CharField(max_length=12, choices=ACCOUNT_TYPES)

    @property
    def total_deposits(self):
        return self.deposits.aggregate(models.Sum('amount'))['amount__sum']

    @property
    def total_invested(self):
        return self.transactions.annotate(
            transaction_cost=models.F('price') * models.F('quantity')
        ).aggregate(models.Sum('transaction_cost'))['transaction_cost__sum']

    @property
    def available_capital(self):
        return self.total_deposits - self.total_invested

    @property
    def nb_shares(self):
        return self.transactions.aggregate(
            models.Sum('quantity')
        )['quantity__sum']

    def __str__(self):
        return self.label


class Deposit(models.Model):
    account = models.ForeignKey(
        'accounts.Account',
        on_delete=models.CASCADE,
        related_name='deposits'
    )
    amount = models.FloatField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'${self.amount} → {self.account} @ {self.date.strftime("%Y-%M-%D %H:%m")}'

