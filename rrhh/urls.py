from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gestor/', views.gestor_rrhh, name='gestor_rrhh'),
]
