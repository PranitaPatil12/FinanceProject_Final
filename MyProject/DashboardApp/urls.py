from django.urls import path,include
from . import views

urlpatterns = [
    path('dashboard/',views.dashboardView, name="adminhomepg"),
    path('cust/', include('Customer.urls')),
    path('address/', include('AddressApp.urls')),
    path('prevloan/', include('PrevLoan.urls')),
    path('loandetail/', include('LoanApplication.urls')),
    path('bankdetail/', include('BankDetails.urls')),
    path('guarantor/', include('customer_guarantor_app.urls')),
    path('professional/', include('ProfessionalDetails.urls')),
    path('document/',include('DocumentApp.urls')),
    path('custdetail/', views.customerdetailview, name='customerdetail'),
    path('custdetail1/', views.personaldetailview, name='personaldetail'),
    path('custdetail2/', views.bankdetailview, name='bankdetail'),
    path('custdetail3/', views.pevloandetailview, name='perloandetail'),
    path('custdetail4/', views.uploaddetailview, name='uploaddetail'),
    path('custdetail5/', views.addressdetailview, name='addressdetail')
]