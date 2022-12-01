from django.contrib import admin

from savings.transactions.models import Exchange, Security, Transaction
from savings.services import percentage_to_display, money_amount_to_display


@admin.register(Exchange)
class ExchangeAdmin(admin.ModelAdmin):
    pass


@admin.register(Security)
class SecurityAdmin(admin.ModelAdmin):
    def price(self, obj):
        return money_amount_to_display(obj.price)

    def day_pl(self, obj):
        return percentage_to_display(obj.day_pl)

    fieldsets = (
        ('Basic informations', {
            'fields': (
                'ticker',
                'exchange',
            )
        }),
        ('Stats', {
            'fields': ('price', 'day_pl')
        }),
    )
    readonly_fields = ('price', 'day_pl')


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    def cost(self, obj):
        return money_amount_to_display(obj.cost)

    fieldsets = (
        ('Basic informations', {
            'fields': (
                'account',
                'security',
                'quantity',
                'price',
                'side',
                'date',
            )
        }),
        ('Stats', {
            'fields': ('cost',)
        }),
    )
    readonly_fields = ('cost',)
