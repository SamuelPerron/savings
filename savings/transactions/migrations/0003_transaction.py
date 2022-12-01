# Generated by Django 4.1.3 on 2022-12-01 01:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_deposit_date'),
        ('transactions', '0002_alter_security_options_position'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField(default=0)),
                ('price', models.FloatField(default=0)),
                ('side', models.CharField(choices=[('buy', 'Buy'), ('sell', 'Sell')], max_length=4)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='accounts.account')),
                ('security', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='transactions.security')),
            ],
        ),
    ]