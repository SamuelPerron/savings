from django.contrib import admin

from savings.transactions.models import Exchange, Security, Transaction


@admin.register(Exchange)
class ExchangeAdmin(admin.ModelAdmin):
    pass


@admin.register(Security)
class SecurityAdmin(admin.ModelAdmin):
    pass


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
