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
    def current_value(self):
        return sum(
            [position.current_value for position in self.positions.all()]
        )

    @property
    def nb_shares(self):
        return self.transactions.aggregate(
            models.Sum('quantity')
        )['quantity__sum']

    @property
    def day_pl(self):
        return sum(
            [position.day_pl for position in self.positions.all()]
        )

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


class Position(models.Model):
    account = models.ForeignKey(
        'accounts.Account',
        on_delete=models.CASCADE,
        related_name='positions',
    )
    security = models.ForeignKey(
        'transactions.Security',
        on_delete=models.CASCADE,
        related_name='positions'
    )
    target_allocation = models.FloatField(default=0)
    is_fractional = models.BooleanField(default=False)
    leftovers = models.FloatField(default=0)

    @property
    def nb_shares(self):
        return self.account.transactions.filter(
            security_id=self.security_id
        ).aggregate(models.Sum('quantity'))['quantity__sum']

    @property
    def total_invested(self):
        return self.account.transactions.filter(
            security_id=self.security_id
        ).annotate(
            transaction_cost=models.F('price') * models.F('quantity')
        ).aggregate(models.Sum('transaction_cost'))['transaction_cost__sum']

    @property
    def current_allocation(self):
        account_total_invested = self.account.total_invested
        total_invested = self.total_invested

        if not total_invested or not account_total_invested:
            return 0

        return total_invested / account_total_invested

    @property
    def current_value(self):
        return self.nb_shares * self.security.price

    @property
    def day_pl(self):
        return self.nb_shares * self.security.day_pl

    @property
    def cost_basis(self):
        nb_shares = self.nb_shares
        total_invested = self.total_invested

        if not total_invested or not nb_shares:
            return 0

        return total_invested / nb_shares

    def __str__(self):
        return f'{self.security} → {self.account}'

