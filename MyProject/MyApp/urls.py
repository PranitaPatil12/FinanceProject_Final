from django.urls import path
from .views import *

urlpatterns = [
    path('home/',homeView, name="homepage"),
    path('nav/el/',eligibility_view,name='eligibility'),
    path('nav/fet/',feature_view,name='features'),
    path('nav/fee/',fees_charges_view,name='fee_charges'),
    path('nav/doc/',req_doc_view,name='req_doc'),
    path('login', login_view, name="loginpage"),
    path('nav/emi/',emi_view,name="emipage"),
    path('about/',about_view, name='aboutpage'),
    path('addloan/',loandetailsView,name='addloan'),
    path('showloandetails/',show_loandetailsView,name='showloandetails'),
    path('update/<int:i>/',update_loandetails,name='update'),
    path('delete/<int:i>/',delete_loandetails,name='delete'),
    path('aenquiry/',EnquiryView,name="aEnquirypg"),
    path('senquiry/',ShowEnquiryView,name='sEnquirypg'),
    path('denquiry/<int:i>/',deleteEnquiryView,name='dEnquirypg'),
    path('approve/<int:i>/',approve_view, name="approve")


]