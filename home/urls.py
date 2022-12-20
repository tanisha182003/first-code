
from django.urls import path,include
from . import views
urlpatterns = [
   
    path('', views.index, name='index' ),
    path('allemp', views.allemp,name='allemp'),
    path('addemp', views.addemp
    ,name='addemp'),
    path('removeemp', views.removeemp,name='removeemp'),
    path('removeemp/<int:emp_id>', views.removeemp,name='removeemp'),

    path('filteremp', views.filteremp,name='filteremp'),
   
]