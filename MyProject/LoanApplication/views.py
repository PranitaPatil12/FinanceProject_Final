from django.shortcuts import render, redirect
from .models import SanctionedLoan
from MyApp.models import LoanDetails
from .forms import SanctionedLoanModelForm, RSanctionedLoanModelForm
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from Customer.models import Customer
from xhtml2pdf import pisa


def home_view(request):
    return render(request, template_name='index.html')


def create_sanctionedoan_view(request,i):
    customer = Customer.objects.get(id=i)
    form = RSanctionedLoanModelForm(initial={'customer':customer})
    if request.user.status == 'OPERATION HEAD':
        form = SanctionedLoanModelForm()
    if request.method == 'POST':
        form = RSanctionedLoanModelForm(request.POST)
        if request.user.status == 'OPERATION HEAD':
            form = SanctionedLoanModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_sanction')
    template_name = 'DashboardApp/sanctioned_loan.html'
    context = {'form': form}
    return render(request, template_name, context)


def show_sanctionedoan_view(request):
    sanction_obj = SanctionedLoan.objects.all()
    template_name = 'DashboardApp/show_sanctioned_loan.html'
    context = {'sanction_obj': sanction_obj}
    return render(request, template_name, context)


def update_sanctionedoan_view(request, i):
    sanction_obj = SanctionedLoan.objects.get(id=i)
    form = SanctionedLoanModelForm(instance=sanction_obj)
    if request.method == 'POST':

        form = SanctionedLoanModelForm(request.POST, instance=sanction_obj)
        if form.is_valid():
            form.save()
            loan = SanctionedLoan.objects.get(id=i)
            loan.is_approved = True
            loan.emi = calculate_emi(loan)
            print(loan)
            print(loan.is_approved)
            loan.save()
            return redirect('show_sanction')
    template_name = 'DashboardApp/sanctioned_loan.html'
    context = {'form': form}
    return render(request, template_name, context)


def get_data(loan):
    data = {
        "app_no": loan.customer.id,
        "amount": loan.approved_loan,
        "interest": loan.interest,
        "tenure": loan.tenure,
        "emi": loan.emi,
        "email": loan.customer.email,
        "mobile": loan.customer.mobile,
        "name":loan.customer.full_name,
    }
    return data


class ViewPDF(View):
    def get(self, request, pk, *args, **kwargs):
        loan = SanctionedLoan.objects.get(id=pk)
        data = get_data(loan)
        pdf = render_to_pdf('DashboardApp/pdf_template.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


# Automaticly downloads to PDF file
class DownloadPDF(View):
    def get(self, request,pk, *args, **kwargs):
        loan = SanctionedLoan.objects.get(id=pk)
        data = get_data(loan)
        pdf = render_to_pdf('DashboardApp/pdf_template.html', data)
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Invoice_%s.pdf" % ("12341231")
        content = "attachment; filename='%s'" % (filename)
        response['Content-Disposition'] = content
        return response


def index(request, pk):
    loan = SanctionedLoan.objects.get(id=pk)

    return render(request, 'DashboardApp/index.html', context={'loan': loan})


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


def calculate_emi(loan):
    print(loan.tenure)
    tenure = loan.tenure
    interest = loan.interest / 12 / 100
    amount = loan.approved_loan
    i = (interest + 1) ** tenure
    p = i - 1.0
    emi = amount * interest * (i / p)
    emi = round(emi, 2)
    return emi
