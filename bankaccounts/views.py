from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import BankAccountForm
from .models import BankAccount


def create_account(request):
     if request.method == 'POST':
         form = BankAccountForm(request.POST)
         if form.is_valid():
             form.save()
             return redirect('/')
     else:
         form = BankAccountForm()
     return render(request, 'form.html', {'form': form})

def update_bank_account(request, p_id):
    b = BankAccount.objects.get(pk=p_id)
    if request.method == 'POST':
        form = BankAccountForm(request.POST, instance=b)
        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = BankAccountForm()
    return render(request, 'form.html', {'form': form})

def delete_bank_account(request, p_id):
     BankAccount.objects.get(pk=p_id).delete()
     return redirect('/')
