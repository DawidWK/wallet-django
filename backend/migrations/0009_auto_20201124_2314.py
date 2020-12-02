# Generated by Django 3.1.3 on 2020-11-24 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_auto_20201124_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='currency_paid_price_in_usd',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='currency_recived_price_in_usd',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='dollar_price_in_pln',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='btc_balance',
            field=models.DecimalField(decimal_places=8, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='eth_balance',
            field=models.DecimalField(decimal_places=8, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='pln_balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='total_balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='usd_balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='xrp_balance',
            field=models.DecimalField(decimal_places=8, default=0, max_digits=15),
        ),
    ]
