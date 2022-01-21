from django.urls import path
from .views import *

urlpatterns = [
    #path('', home_view, name='homepage'),
    path('create/<int:i>/', create_sanctionedoan_view, name='create_sanction'),
    path('showsanctionloan',show_sanctionedoan_view,name='show_sanction'),
    path('updatesanctionloan/<int:i>/',update_sanctionedoan_view,name='update_sanction'),
    path('index/<int:pk>', index, name='index'),
    path('pdf_view/<int:pk>', ViewPDF.as_view(), name="pdf_view"),
    path('pdf_download/<int:pk>', DownloadPDF.as_view(), name="pdf_download"),

]
