from django.shortcuts import render,redirect
from .models import Customer
from .forms import CustomerModelForm

def dashboardView(request):
    return render(request,"DashboardApp/base.html")

def dashboardView(request):
    return render(request,"DashboardApp/base.html")


def customerdetailview(request):
    return render(request,"DashboardApp/customerdetail.html")

def bankdetailview(request):
    return render(request,"DashboardApp/bankTable.html")

def uploaddetailview(request):
    return render(request,"DashboardApp/uploadTable.html")

def pevloandetailview(request):
    return render(request,"DashboardApp/prvloanTable.html")

def personaldetailview(request):
    return render(request,"DashboardApp/personalTable.html")

def addressdetailview(request):
    return render(request,"DashboardApp/addressTable.html")
