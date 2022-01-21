from django.urls import path
from . import views


urlpatterns =[
    path('log',views.loginview,name='loginpage1'),
    path('out',views.logoutview,name='logout')
]