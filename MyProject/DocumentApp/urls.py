from django.urls import path
from . import views

urlpatterns = [
    path('cDocument/<int:i>/',views.create_document_view),
]