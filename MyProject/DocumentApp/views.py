from django.shortcuts import render,redirect
from .models import Documents
from .forms import DocumentsForm
from Customer.models import Customer


# Create your views here.
def create_document_view(request,i):
    customer = Customer.objects.get(id=i)
    form = DocumentsForm(initial={'customer':customer})
    if request.method == 'POST':
        form = DocumentsForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/dapp/loandetail/create/%i' % customer.id)
    template_name = 'DashboardApp/document.html'
    context = {'form':form}
    return render(request,template_name,context)


