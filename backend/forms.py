from django import forms
from .models import Wallet, Transaction

class NewWalletForm(forms.ModelForm):
    class Meta:
        model = Wallet
        fields = [
            'name', 
            'pln_balance',
            # 'usd_balance',
            'btc_balance',
            'xrp_balance',
            'eth_balance'
        ]
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'pln_balance': forms.NumberInput(attrs={'class': 'form-control'}),
            # 'usd_balance': forms.NumberInput(attrs={'class': 'form-control'}),
            'btc_balance': forms.NumberInput(attrs={'class': 'form-control'}),
            'xrp_balance': forms.NumberInput(attrs={'class': 'form-control'}),
            'eth_balance': forms.NumberInput(attrs={'class': 'form-control'}),
        }

            

class NewTransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'

        labels = {
            'currency_paid_price_in_pln': 'Currency-paid price in PLN (OPTIONAL)',
            'currency_recived_price_in_pln': 'Currency-recived price in PLN (OPTIONAL)', 
            'dollar_price_in_pln': 'Dollar price in PLN (OPTIONAL)',
        }

        widgets = {
            'wallet': forms.Select(attrs={'class': 'form-control'}),
            'currency_paid': forms.Select(attrs={'class': 'form-control'}),
            'amount_paid':forms.NumberInput(attrs={'class': 'form-control'}),
            'currency_recived': forms.Select(attrs={'class': 'form-control'}),
            'amount_recived': forms.NumberInput(attrs={'class': 'form-control'}),
            'date': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),            
            'currency_paid_price_in_pln': forms.NumberInput(attrs={'class': 'form-control'}),
            'currency_recived_price_in_pln': forms.NumberInput(attrs={'class': 'form-control'}),
            'dollar_price_in_pln': forms.NumberInput(attrs={'class': 'form-control'}),
        }