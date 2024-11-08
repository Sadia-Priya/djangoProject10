from django.shortcuts import render

from bankaccounts.models import BankAccount


def home(request):
    bankaccounts = BankAccount.objects.all()
    return render(request, 'home.html', {'bankaccounts': bankaccounts})