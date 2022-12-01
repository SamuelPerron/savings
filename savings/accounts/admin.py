from django.contrib import admin

from savings.accounts.models import Source, Account, Deposit, Position
from savings.services import percentage_to_display, money_amount_to_display


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    pass


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    def day_pl(self, obj):
        return percentage_to_display(obj.day_pl)

    def roi(self, obj):
        return percentage_to_display(obj.roi)

    def total_deposits(self, obj):
        return money_amount_to_display(obj.total_deposits)

    def total_invested(self, obj):
        return money_amount_to_display(obj.total_invested)

    def available_capital(self, obj):
        return money_amount_to_display(obj.available_capital)

    def current_value(self, obj):
        return money_amount_to_display(obj.current_value)

    fieldsets = (
        ('Basic informations', {
            'fields': ('source', 'user', 'label', 'account_type')
        }),
        ('Stats', {
            'fields': (
                'total_deposits',
                'total_invested',
                'available_capital',
                'nb_shares',
                'day_pl',
                'current_value',
                'roi',
            )
        }),
    )
    readonly_fields = (
        'total_deposits',
        'total_invested',
        'available_capital',
        'nb_shares',
        'day_pl',
        'current_value',
        'roi',
    )



@admin.register(Deposit)
class DepositAdmin(admin.ModelAdmin):
    pass


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    def day_pl(self, obj):
        return percentage_to_display(obj.day_pl)

    def roi(self, obj):
        return percentage_to_display(obj.roi)

    def current_allocation(self, obj):
        return percentage_to_display(obj.current_allocation)

    def total_invested(self, obj):
        return money_amount_to_display(obj.total_invested)

    def cost_basis(self, obj):
        return money_amount_to_display(obj.cost_basis)

    def current_value(self, obj):
        return money_amount_to_display(obj.current_value)

    fieldsets = (
        ('Basic informations', {
            'fields': (
                'account',
                'security',
                'target_allocation',
                'is_fractional',
            )
        }),
        ('Stats', {
            'fields': (
                'nb_shares',
                'total_invested',
                'current_allocation',
                'cost_basis',
                'day_pl',
                'current_value',
                'roi',
            )
        }),
    )
    readonly_fields = (
        'nb_shares',
        'total_invested',
        'current_allocation',
        'cost_basis',
        'day_pl',
        'current_value',
        'roi',
    )
