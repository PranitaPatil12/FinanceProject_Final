from django.shortcuts import render, redirect
from .models import ProfessionalDetails
from .forms import SalariedModelForm, SelfSalariedModelForm
from Customer.models import Customer


# Create your views here.


def AddSalariedView(request,i):
    customer = Customer.objects.get(id=i)
    form = SalariedModelForm(initial={'type_employment':'SALARIED','customer':customer})
    if request.method == 'POST':
        form = SalariedModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/dapp/bankdetail/cBankDetails/%i' % customer.id)
        else:
            print('Form is INVALID')
    context = {'form': form}
    templates_name = 'DashboardApp/add_sal.html'
    return render(request, templates_name, context)

def ShowSalariedView(request):
    show_obj = ProfessionalDetails.objects.all()
    context = {'show_obj': show_obj}
    templates_name = 'show_sal.html'
    return render(request, templates_name, context)

def UpdateSalariedView(request, i):
    update_obj = ProfessionalDetails.objects.get(id=i)
    form = SalariedModelForm(instance=update_obj)
    if request.method == 'POST':
        form = SalariedModelForm(request.POST, instance=update_obj)
        if form.is_valid():
            form.save()
            return redirect('show_sal')
    context = {'form': form}
    templates_name = 'add_sal.html'
    return render(request, templates_name, context)


def DeleteSalariedView(request, i):
    lap = ProfessionalDetails.objects.get(id=i)
    lap.delete()
    return redirect('show_sal')

# Self-Salried Views

def AddSelfSalariedView(request,i):
    customer = Customer.objects.get(id=i)
    form = SelfSalariedModelForm(initial={'type_employment':'SELF-SALARIED','customer':customer})
    if request.method == 'POST':
        form = SelfSalariedModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/dapp/bankdetail/cBankDetails/%i' % customer.id)
        else:
            print('Form is INVALID')
    context = {'form': form}
    templates_name = 'DashboardApp/add_self.html'
    return render(request, templates_name, context)

def ShowSelfSalariedView(request):
    show_obj = ProfessionalDetails.objects.all()
    context = {'show_obj': show_obj}
    templates_name = 'show_self.html'
    return render(request, templates_name, context)

def UpdateSelfSalariedView(request, i):
    update_obj = ProfessionalDetails.objects.get(id=i)
    form = SelfSalariedModelForm(instance=update_obj)
    if request.method == 'POST':
        form = SelfSalariedModelForm(request.POST, instance=update_obj)
        if form.is_valid():
            form.save()
            return redirect('show_self')

    context = {'form': form}
    templates_name = 'add_self.html'
    return render(request, templates_name, context)

def DeleteSelfSalariedView(request, i):
    lap = ProfessionalDetails.objects.get(id=i)
    lap.delete()
    return redirect('show_self')


# def page(request):
#     # Your code first
#
#     view_value = None
#     if request.method == 'POST':
#         view = request.POST.get('view')
#
#         if view == 'view1':
#             return redirect('add_sal') # If you don't have a context, simply don't include it in this line
#         elif view == 'view2':
#             return redirect('add_self')
#
#         else:
#             render(request, 'DashboardApp/professional_details.html')  # If there's no match, load the default one.
#     return render(request, 'DashboardApp/professional_details.html')

def page1(request,i):
    customer = Customer.objects.get(id=i)
    if request.method == 'GET':
        view = request.GET.get('employmentType')

        if view == 'salaried':
            return redirect('/dapp/professional/addsal/%i' % customer.id) # If you don't have a context, simply don't include it in this line
        elif view == 'self employed':
            return redirect('/dapp/professional/addself/%i' % customer.id)

        else:
            render(request, 'DashboardApp/Profe_detail.html')  # If there's no match, load the default one.
    return render(request, 'DashboardApp/Profe_detail.html')
