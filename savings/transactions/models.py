from django.db import models


class Exchange(models.Model):
    name = models.CharField(max_length=50)
    label = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Security(models.Model):
    ticker = models.CharField(max_length=10)
    exchange = models.ForeignKey(
        'transactions.Exchange',
        on_delete=models.CASCADE,
        related_name='securities'
    )

    def __str__(self):
        return self.ticker

    class Meta:
        verbose_name_plural = 'securities'


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
    def cost_basis(self):
        nb_shares = self.nb_shares
        total_invested = self.total_invested

        if not total_invested or not nb_shares:
            return 0

        return total_invested / nb_shares

    def __str__(self):
        return f'{self.security} → {self.account}'


class Transaction(models.Model):
    BUY = 'buy'
    SELL = 'sell'
    SIDES = (
        (BUY, 'Buy'),
        (SELL, 'Sell')
    )

    account = models.ForeignKey(
        'accounts.Account',
        on_delete=models.CASCADE,
        related_name='transactions'
    )
    security = models.ForeignKey(
        'transactions.Security',
        on_delete=models.CASCADE,
        related_name='transactions'
    )
    quantity = models.FloatField(default=0)
    price = models.FloatField(default=0)
    side = models.CharField(
        max_length=4,
        choices=SIDES
    )
    date = models.DateTimeField(null=True)

    @property
    def cost(self):
        return self.quantity * self.price

    def __str__(self):
        return f'{self.side.upper()} {self.quantity} {self.security} @ {self.price}'
