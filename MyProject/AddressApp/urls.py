from django.urls import path
from . import views

urlpatterns =[
    path('cAddress/<int:i>',views.create_address_view,name='cAddresspg'),
    path('sAddress/',views.show_address_view,name='sAddresspg'),
    path('uAddress/<int:i>/',views.update_address_view,name='uAddresspg'),
    path('dAddress/<int:i>/',views.delete_address_view,name='dAddresspg')

]