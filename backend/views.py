from django.shortcuts import render
from .models import Wallet, Transaction


from django.http import HttpResponseRedirect
from .forms import NewWalletForm, NewTransactionForm
# Create your views here.

def wallet_page(request, wallet_name):
    current_wallet = Wallet.objects.get(name=wallet_name)
    wallets = Wallet.objects.all()
    new_wallet_form = NewWalletForm()
    new_transaction_form = NewTransactionForm()

    context = {
        'new_wallet_form': new_wallet_form,
        'new_transaction_form': new_transaction_form,
        'wallets': wallets,
        'current_wallet': current_wallet,
    }
    return render(request, 'main/wallet.html', context)

def home(request):
    wallets = Wallet.objects.all()
    new_wallet_form = NewWalletForm()

    context = {
        'new_wallet_form': new_wallet_form,
        'wallets': wallets,
    }

    return render(request, 'main/home.html', context)

def home_err(request, exception):
    return HttpResponseRedirect('/')

def home_err500(request):
    return HttpResponseRedirect('/')


def add_wallet(request):
    if request.method == 'POST':
        form = NewWalletForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/wallet/' + request.POST['name'] + '/')
    return HttpResponseRedirect('/')
   

def delete_wallet(request):
    if request.method == 'POST':
        wallet = Wallet.objects.get(id=request.POST['wallet-id'])
        wallet.delete()
        return HttpResponseRedirect('/wallet/' + request.POST['current-wallet'] + '/')
    return HttpResponseRedirect('/')

def add_transaction(request):
    if request.method == 'POST':
        form = NewTransactionForm(request.POST)
        wallet = Wallet.objects.get(id=request.POST['wallet'])
        if form.is_valid():
            form.save()    
        return HttpResponseRedirect('/wallet/' + wallet.name + '/')
    return HttpResponseRedirect('/')

def delete_transaction(request):
    if request.method == 'POST':
        transaction = Transaction.objects.get(id=request.POST['transaction-id'])
        transaction.delete()
        return HttpResponseRedirect('/wallet/' + request.POST['current-wallet'] + '/')
    return HttpResponseRedirect('/')