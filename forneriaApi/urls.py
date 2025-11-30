from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from forneria import views
from forneriaApi import views as vistasApi
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('empleadosApi/',vistasApi.empleadosApi, name='empleadoApi'),
    path('empleadosListApi/', vistasApi.empleado_listado, name='empleadosListApi'),
    path('empleadosListApi/<int:pk>/', vistasApi.empleado_detalle),
    path('liquidacionesApi/',vistasApi.liquidacionesApi, name='liquidacionesApi'),
    path('liquidacionesListApi/', vistasApi.liquidacion_listado),
    path('liquidacionesListApi/<int:pk>/', vistasApi.liquidacion_detalle),
    path('cargosApi/',vistasApi.cargosApi, name='cargosApi'),
    path('cargosListApi/', vistasApi.cargo_listado),
    path('cargosListApi/<int:pk>/', vistasApi.cargo_detalle),
    path('contratosApi/',vistasApi.contratosApi, name='contratosApi'),
    path('contratosListApi/', vistasApi.contrato_listado),
    path('contratosListApi/<int:pk>/', vistasApi.contrato_detalle),
    path('AuthUserApi/',vistasApi.AuthUserApi, name='AuthUserApi'),
    path('usuariosListApi/', vistasApi.usuario_listado),
    path('usuariosListApi/<int:pk>/', vistasApi.usuario_detalle),
]
