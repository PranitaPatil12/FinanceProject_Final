from django.urls import path
from .views import create_bankdetails_view,show_bankdetails_view,update_bankdetails_view,delete_bankdetails_view

urlpatterns=[
    path('cBankDetails/<int:i>/',create_bankdetails_view,name='cBankDetailspg'),
    path('sBankDetails/',show_bankdetails_view,name='sBankDetailspg'),
    path('uBankDetails/<int:i>/',update_bankdetails_view,name='uBankDetailspg'),
    path('dBankDetails/<int:i>/',delete_bankdetails_view,name='dBankDetailspg'),
]