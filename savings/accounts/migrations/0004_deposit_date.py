# Generated by Django 4.1.3 on 2022-12-01 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_deposit'),
    ]

    operations = [
        migrations.AddField(
            model_name='deposit',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
