from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('gestor/', views.gestor_rrhh, name='gestor_rrhh'),
    path('mantenedor_empleados/', views.mantenedor_empleados, name='mantenedor_empleados'),
    path('mantenedor_contratos/', views.mantenedor_contratos, name='mantenedor_contratos'),
    path('mantenedor_usuarios/', views.mantenedor_usuarios, name='mantenedor_usuarios'),
    path('crear_empleado/', views.crear_empleado, name='crear_empleado'),
    path('todos_empleados/', views.todos_empleados, name='todos_empleados'),
    path('editar_empleado/<int:id_empleado>/', views.editar_empleado, name='editar_empleado'),
    path('eliminar_empleado/<int:id_empleado>/', views.eliminar_empleado, name='eliminar_empleado'),
    path('restaurar_empleado/<int:id_empleado>/', views.restaurar_empleado, name='restaurar_empleado'),
    path('todos_cargos/', views.todos_cargos, name='todos_cargos'),
    path('crear_cargo/', views.crear_cargo, name='crear_cargo'),
    path('editar_cargo/<int:id_cargo>/', views.editar_cargo, name='editar_cargo'),
    path('eliminar_cargo/<int:id_cargo>/', views.eliminar_cargo, name='eliminar_cargo'),
    path('restaurar_cargo/<int:id_cargo>/', views.restaurar_cargo, name='restaurar_cargo'),
    path('todos_usuarios/', views.todos_usuarios, name='todos_usuarios'),
    path('crear_usuario/', views.crear_usuario, name='crear_usuario'),
    path('editar_usuario/<int:id_usuario>/', views.editar_usuario, name='editar_usuario'),
    path('eliminar_usuario/<int:id_usuario>/', views.eliminar_usuario, name='eliminar_usuario'),
    path('restaurar_usuario/<int:id_usuario>/', views.restaurar_usuario, name='restaurar_usuario'),
    path('rrhh/desactivar_usuario/<int:id_usuario>/', views.desactivar_usuario, name='desactivar_usuario'),
    path('rrhh/activar_usuario/<int:id_usuario>/', views.activar_usuario, name='activar_usuario'),
    path('rrhh/contratos/', views.listar_contratos, name='listar_contratos'),
    path('rrhh/contratos/crear/', views.crear_contrato, name='crear_contrato'),
    path('rrhh/contratos/editar/<int:contrato_id>/', views.editar_contrato, name='editar_contrato'),
    path('rrhh/contratos/eliminar/<int:contrato_id>/', views.eliminar_contrato, name='eliminar_contrato'),
    path('rrhh/contratos/restaurar/<int:contrato_id>/', views.restaurar_contrato, name='restaurar_contrato'),
    path('rrhh/liquidaciones/', views.listar_liquidaciones, name='listar_liquidaciones'),
    path('rrhh/liquidaciones/crear/', views.crear_liquidacion, name='crear_liquidacion'),
    path('rrhh/liquidaciones/editar/<int:id>/', views.editar_liquidacion, name='editar_liquidacion'),
    path('rrhh/liquidaciones/eliminar/<int:liquidacion_id>/', views.eliminar_liquidacion, name='eliminar_liquidacion'),
    path('rrhh/liquidaciones/restaurar/<int:liquidacion_id>/', views.restaurar_liquidacion, name='restaurar_liquidacion'),

]
