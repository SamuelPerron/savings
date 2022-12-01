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
