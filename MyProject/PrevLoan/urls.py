from django.urls import path
from . import views

urlpatterns = [
    path('cPrevLoan/<int:i>/',views.create_prevloan_view,name='cPrevLoanpg'),
    path('rPrevLoan/',views.show_prevloan_view,name='rPrevLoanpg'),
    path('dPrevLoan/<int:i>/',views.delete_prevloan_view,name='dPrevLoanpg'),
    path('uPrevLoan/<int:i>/',views.update_prevloan_view,name='uPrevLoanpg'),
    path('ploanConfirm/<int:i>/',views.prev_loan_confirmation,name='ploanConfirm')
]