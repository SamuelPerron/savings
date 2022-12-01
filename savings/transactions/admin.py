from django.contrib import admin

from savings.transactions.models import Exchange, Position, Security, Transaction


@admin.register(Exchange)
class ExchangeAdmin(admin.ModelAdmin):
    pass


@admin.register(Security)
class SecurityAdmin(admin.ModelAdmin):
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
            )
        }),
    )
    readonly_fields = (
        'nb_shares',
        'total_invested',
        'current_allocation',
        'cost_basis',
    )


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
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
