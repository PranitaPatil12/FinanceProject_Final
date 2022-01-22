from django.shortcuts import render,redirect
from .models import Customer
from .forms import CustomerForm
from AddressApp.models import PermanentAddress
from customer_guarantor_app.models import Guarantor
from BankDetails.models import BankDetails
from LoanApplication.models import SanctionedLoan
from PrevLoan.models import PrevLoan
from ProfessionalDetails.models import ProfessionalDetails
from DocumentApp.models import Documents
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
import random



form1 = None
otp = None
user = None
def create_customer_view(request):
    form = CustomerForm()
    if request.method == 'POST' and 'submit' in request.POST:
        form = CustomerForm(request.POST)
        if form.is_valid():
            print("1--form valid", request.POST)
            # global user
            full_name = request.POST['full_name']
            email = request.POST['email']
            global form1
            form1 = form.save(commit=False)
            global otp
            otp = random.randint(1000, 9999)
            subject = 'verification otp'
            message = f'Hi {full_name}, thank you for Personal Loan Registration.Your email verification OTP is {otp}'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email, ]
            send_mail(subject, message, email_from, recipient_list)
            print("otp", otp)
            return redirect('sOtppg')


    template_name = 'DashboardApp/personaldetail.html'
    context = {'form':form}
    return render(request,template_name,context)



def OTPVerifyView(request):
    if request.method == 'POST':
        num = request.POST.get('otp')
        print('num',num)
        global form1
        if  int(num) == otp:
            print("1--form valid otp", request.POST)
            form1.save()
            return redirect("/dapp/address/cAddress/%i" % form1.id)

        else:
            messages.error(request, "Invalid otp")
            return redirect('cCustomerpg')

    template_name = 'DashboardApp/otpverify.html'
    context = {}
    return render(request, template_name, context)

def show_customer_view(request):
    customer = Customer.objects.all()
    template_name = 'DashboardApp/showCustomer.html'
    context = {'customer':customer}
    return render(request,template_name,context)

def show_details_view(request,i):
    customer = Customer.objects.get(id=i)
    # guarantor = Guarantor.objects.get(customer=customer)
    paddress = PermanentAddress.objects.get(customer=customer)
    bankdetails = BankDetails.objects.get(customer=customer)
    loansanction = SanctionedLoan.objects.get(customer=customer)
    prevloan = PrevLoan.objects.filter(customer=customer)
    # profdetails =ProfessionalDetails.objects.get(customer=customer)
    docu = Documents.objects.get(customer=customer)
    template_name = 'DashboardApp/customerdetail.html'
    context = {'customer': customer,
                'prevloan':prevloan,
                'bankdetails': bankdetails,
               'paddress':paddress,'loansanction':loansanction,'docu':docu}

    return render(request, template_name, context)

