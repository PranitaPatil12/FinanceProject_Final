from django.urls import path
from . import views

urlpatterns=[
    path('addsal/<int:i>/', views.AddSalariedView, name='add_sal'),
    path('showsal/', views.ShowSalariedView, name='show_sal'),
    path('update_sal/<int:i>', views.UpdateSalariedView, name='update_sal'),
    path('delete_sal/<int:i>', views.DeleteSalariedView, name='delete_sal'),

    path('addself/<int:i>/', views.AddSelfSalariedView, name='add_self'),
    path('showself/', views.ShowSelfSalariedView, name='show_self'),
    path('update_self/<int:i>', views.UpdateSelfSalariedView, name='update_self'),
    path('delete_self/<int:i>', views.DeleteSelfSalariedView, name='delete_self'),
    # path('page/', views.page,name='page'),
    path('page1/<int:i>/', views.page1,name='page1')
]