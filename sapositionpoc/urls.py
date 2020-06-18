from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test/', views.test, name='test'),
    path('sa_form/', views.sa_form_view, name='sa_form'),
    path('saquery/', views.saquery, name='saquery'),
    path('saresult/', views.saresult, name='saresult'),
]
