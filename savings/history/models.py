from django.db import models


class AccountData(models.Model):
    account = models.ForeignKey(
        'accounts.Account',
        on_delete=models.CASCADE,
        related_name='data_points'
    )

    time = models.DateTimeField(auto_now=True)

    total_deposits = models.FloatField()
    total_invested = models.FloatField()
    available_capital = models.FloatField()
    current_value = models.FloatField()
    nb_shares = models.FloatField()
    roi = models.FloatField()


