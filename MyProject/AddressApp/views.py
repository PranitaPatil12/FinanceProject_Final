from django.shortcuts import render,redirect
from .models import PermanentAddress,CurrentAddress
from .forms import PermanentAddressForm,CurrentAddressForm
from Customer.models import Customer

# Create your views here.

def create_address_view(request,i):
    customer = Customer.objects.get(id=i)
    form = PermanentAddressForm(initial={'customer':customer})
    form_1 = CurrentAddressForm(initial={'customer':customer})
    if request.method == 'POST':
        form = PermanentAddressForm(request.POST)
        form_1 = CurrentAddressForm(request.POST)
        if form.is_valid() and form_1.is_valid():
            form.save()
            form_1.save()
            return redirect('/dapp/professional/page1/%i' % customer.id)
    template_name = 'DashboardApp/addAddress.html'
    context = {'form':form,'form_1':form_1}
    return render(request, template_name, context)


def show_address_view(request):
    paddr = PermanentAddress.objects.all()
    caddr = CurrentAddress.objects.all()
    template_name = 'AddressApp/showAddress.html'
    context = {'paddr': paddr, 'caddr':caddr}
    return render(request, template_name, context)


def update_address_view(request,i):
    paddr = PermanentAddress.objects.get(id=i)
    form = PermanentAddressForm(instance=paddr)
    caddr = CurrentAddress.objects.get(id=i)
    form_1 = CurrentAddressForm(instance=caddr)
    if request.method == 'POST':
        form = PermanentAddressForm(request.POST, instance=paddr)
        form_1 = CurrentAddressForm(request.POST,instance=caddr)
        if form.is_valid() and form_1.is_valid() :
            form.save()
            form_1.save()
            return redirect('sAddresspg')
    template_name = 'AddressApp/addAddress.html'
    context = {'form': form,'form_1':form_1}
    return render(request, template_name, context)


def delete_address_view(request,i):
    paddr = PermanentAddress.objects.get(id=i)
    caddr = CurrentAddress.objects.get(id=i)
    if request.method == 'POST':
        paddr.delete()
        caddr.delete()
        return redirect('sAddresspg')
    template_name = 'AddressApp/deleteAddress.html'
    context = {'paddr': paddr,'caddr':caddr}
    return render(request, template_name, context)