from django.contrib import admin

from savings.accounts.models import Source, Account, Deposit, Position


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    pass


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
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
    )



@admin.register(Deposit)
class DepositAdmin(admin.ModelAdmin):
    pass


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
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
    )
