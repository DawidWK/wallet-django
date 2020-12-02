from django.db import models
from django.db.models.signals import post_save, pre_save, pre_delete
from django.dispatch import receiver
from django.utils import timezone

import cryptocompare

# Create your models here.

CURRENCY = (
    ('PLN', 'PLN'),
    # ('USD', 'USD'),
    ('BTC', 'BTC'),
    ('XRP', 'XRP'),
    ('ETH', 'ETH'),
)

class Wallet(models.Model):
    name = models.CharField(max_length=50)
    total_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    pln_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    # usd_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    btc_balance = models.DecimalField(max_digits=15, decimal_places=8, default=0)
    xrp_balance = models.DecimalField(max_digits=15, decimal_places=8, default=0)
    eth_balance = models.DecimalField(max_digits=15, decimal_places=8, default=0)

    def __str__(self):
        return self.name

    def get_btc_in_pln(self):
        return round(float(self.btc_balance) * cryptocompare.get_price('BTC',curr='PLN')['BTC']['PLN'], 2)

    def get_xrp_in_pln(self):
        return round(float(self.xrp_balance) * cryptocompare.get_price('XRP',curr='PLN')['XRP']['PLN'], 2)

    def get_eth_in_pln(self):
        return round(float(self.eth_balance) * cryptocompare.get_price('ETH',curr='PLN')['ETH']['PLN'], 2)

    def get_total_balance(self):
        btc_price = cryptocompare.get_price('BTC',curr='PLN')['BTC']['PLN']
        xrp_price = cryptocompare.get_price('XRP',curr='PLN')['XRP']['PLN']
        eth_price = cryptocompare.get_price('ETH',curr='PLN')['ETH']['PLN']

        pln_balance = float(self.pln_balance)
        # usd_balance = float(self.usd_balance)
        btc_balance = float(self.btc_balance)
        xrp_balance = float(self.xrp_balance)
        eth_balance = float(self.eth_balance)

        self.total_balance = pln_balance + round(btc_balance * btc_price, 2) + round(xrp_balance * xrp_price, 2) + round(eth_balance * eth_price,2)
        return round(self.total_balance, 2)

class Transaction(models.Model):
    # NECESSARY
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    currency_paid = models.CharField(choices=CURRENCY, max_length=3)
    amount_paid = models.DecimalField(max_digits=15, decimal_places=8)
    currency_recived = models.CharField(choices=CURRENCY, max_length=3)
    amount_recived = models.DecimalField(max_digits=15, decimal_places=8)
    date = models.DateTimeField(default=timezone.now)
    description = models.TextField(max_length=250)
    
    # OPTIONAL
    currency_paid_price_in_pln = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    currency_recived_price_in_pln = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    dollar_price_in_pln = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return "id: " + str(self.id) + " " + str(self.currency_paid) + " -> " + str(self.currency_recived)


# SIGNALS
@receiver(post_save, sender=Transaction)
def create_transaction(sender, instance, created, **kwargs):
    if created:
        wallet = Wallet.objects.get(name = instance.wallet)

        currency_paid = instance.currency_paid
        currency_recived = instance.currency_recived
        amount_paid = instance.amount_paid
        amount_recived = instance.amount_recived

        # SUBSTRACK BALANCE
        if(currency_paid == 'PLN'):
            wallet.pln_balance -= amount_paid
        elif(currency_paid == 'USD'):
            wallet.usd_balance -= amount_paid
        elif(currency_paid == 'BTC'):
            wallet.btc_balance -= amount_paid
        elif(currency_paid == 'XRP'):
            wallet.xrp_balance -= amount_paid
        elif(currency_paid == 'ETH'):
            wallet.eth_balance -= amount_paid

        # ADDS BALANCE
        if(currency_recived == 'PLN'):
            wallet.pln_balance += amount_recived
        elif(currency_recived == 'USD'):
            wallet.usd_balance += amount_recived
        elif(currency_recived == 'BTC'):
            wallet.btc_balance += amount_recived
        elif(currency_recived == 'XRP'):
            wallet.xrp_balance += amount_recived
        elif(currency_recived == 'ETH'):
            wallet.eth_balance += amount_recived

        wallet.save()

@receiver(pre_delete, sender=Transaction)
def delete_transaction(sender, instance, **kwargs):
    wallet = Wallet.objects.get(name = instance.wallet)

    currency_paid = instance.currency_paid
    currency_recived = instance.currency_recived
    amount_paid = instance.amount_paid
    amount_recived = instance.amount_recived

    if(currency_paid == 'PLN'):
        wallet.pln_balance += amount_paid
    elif(currency_paid == 'USD'):
        wallet.usd_balance += amount_paid
    elif(currency_paid == 'BTC'):
        wallet.btc_balance += amount_paid
    elif(currency_paid == 'XRP'):
        wallet.xrp_balance += amount_paid
    elif(currency_paid == 'ETH'):
        wallet.eth_balance += amount_paid

    if(currency_recived == 'PLN'):
        wallet.pln_balance -= amount_recived
    elif(currency_recived == 'USD'):
        wallet.usd_balance -= amount_recived
    elif(currency_recived == 'BTC'):
        wallet.btc_balance -= amount_recived
    elif(currency_recived == 'XRP'):
        wallet.xrp_balance -= amount_recived
    elif(currency_recived == 'ETH'):
        wallet.eth_balance -= amount_recived

    wallet.save()


@receiver(pre_save, sender=Wallet)
def total_balance_update(sender, instance, **kwargs):
    btc_price = cryptocompare.get_price('BTC',curr='PLN')['BTC']['PLN']
    xrp_price = cryptocompare.get_price('XRP',curr='PLN')['XRP']['PLN']
    eth_price = cryptocompare.get_price('ETH',curr='PLN')['ETH']['PLN']


    pln_balance = float(instance.pln_balance)
    # usd_balance = float(instance.usd_balance)
    btc_balance = float(instance.btc_balance)
    xrp_balance = float(instance.xrp_balance)
    eth_balance = float(instance.eth_balance)

    instance.total_balance = pln_balance + round(btc_balance * btc_price, 2) + round(xrp_balance * xrp_price, 2) + round(eth_balance * eth_price, 2)
    
