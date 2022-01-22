from django.shortcuts import render, redirect
from .forms import PrevLoanForm
from .models import PrevLoan
from Customer.models import Customer


def create_prevloan_view(request,i):
    customer = Customer.objects.get(id=i)
    form = PrevLoanForm(initial={'customer':customer})
    if request.method == 'POST':
        form = PrevLoanForm(request.POST)
        if form.is_valid():
            form.save()
            r = request.POST.get("add")
            if r == 'Add more Detail':
                return redirect('/dapp/prevloan/cPrevLoan/%i' % customer.id)
            return redirect('/dapp/guarantor/add_guarantor/%i' % customer.id)
    template_name = 'DashboardApp/prevloandetails.html'
    context = {'form': form}
    return render(request, template_name, context)


def show_prevloan_view(request):
    bank = PrevLoan.objects.all()
    template_name = 'show.html'
    context = {'bank': bank}
    return render(request, template_name, context)


def delete_prevloan_view(request, i):
    bank = PrevLoan.objects.get(id=i)
    bank.delete()
    return redirect('rPrevLoanpg')


def update_prevloan_view(request, i):
    bank = PrevLoan.objects.get(id=i)
    form = PrevLoanForm(instance=bank)
    if request.method == 'POST':
        form = PrevLoanForm(request.POST, instance=bank)
        if form.is_valid():
            form.save()
            return redirect('rPrevLoanpg')
    context = {'form': form}
    template_name = 'add.html'
    return render(request, template_name, context)

def prev_loan_confirmation(request,i):
    customer = Customer.objects.get(id=i)
    template_name = 'DashboardApp/prev_loan_confirmation.html'
    context = {'customer':customer}
    return render(request, template_name, context)

