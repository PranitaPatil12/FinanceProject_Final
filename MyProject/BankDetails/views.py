from django.shortcuts import render,redirect
from .models import *
from .forms import *
from Customer.models import Customer

# Create your views here.
def create_bankdetails_view(request,i):
    customer = Customer.objects.get(id=i)
    form = BankDetailsModelForm(initial={'customer':customer})
    if request.method == 'POST':
        form = BankDetailsModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/dapp/prevloan/ploanConfirm/%i' % customer.id)

    context={'form':form}
    return render(request,'DashboardApp/addBankDetails.html',context)

def show_bankdetails_view(request):
    BankDetails_list = BankDetails.objects.all()
    template_name = "showBankDetails.html"
    context = {'BankDetails_list': BankDetails_list}
    return render(request, template_name, context)

def update_bankdetails_view(request,i):
    bank = BankDetails.objects.get(id=i)
    form = BankDetailsModelForm(instance=bank)
    if request.method == 'POST':
        form = BankDetailsModelForm(request.POST,instance=bank)
        if form.is_valid():
            form.save()
            return redirect("sBankDetailspg")
    template_name = "addBankDetails.html"
    context = {'form': form}
    return render(request, template_name, context)

def delete_bankdetails_view(request,i):
    bank= BankDetails.objects.get(id=i)
    bank.delete()
    return redirect("sBankDetailspg")