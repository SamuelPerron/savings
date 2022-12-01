from django.contrib import admin

from savings.accounts.models import Source, Account, Deposit


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
            )
        }),
    )
    readonly_fields = (
        'total_deposits',
        'total_invested',
        'available_capital',
        'nb_shares',
    )



@admin.register(Deposit)
class DepositAdmin(admin.ModelAdmin):
    pass
