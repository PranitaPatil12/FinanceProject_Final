from django.urls import path
from . import views

urlpatterns = [
    path('cCustomer/',views.create_customer_view,name='cCustomerpg'),
    path('sCustomer/',views.show_customer_view,name='sCustomerpg'),
    path('show_customer_details/<int:i>',views.show_details_view,name='show_address'),
    path('otp/',views.OTPVerifyView,name='sOtppg'),
]