from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gestor/', views.gestor_rrhh, name='gestor_rrhh'),
    path('mantenedor_empleados/', views.mantenedor_empleados, name='mantenedor_empleados'),
    path('mantenedor_contratos/', views.mantenedor_contratos, name='mantenedor_contratos'),
    path('mantenedor_usuarios/', views.mantenedor_usuarios, name='mantenedor_usuarios'),
    path('crear_empleado/', views.crear_empleado, name='crear_empleado'),
    path('todos_empleados/', views.todos_empleados, name='todos_empleados'),
    path('cargar_editar_empleado/<int:id_empleado>/', views.cargar_editar_empleado, name='cargar_editar_empleado'),
    path('editar_empleado/<int:id_empleado>/', views.editar_empleado, name='editar_empleado'),
    path('eliminar_empleado/<int:id_empleado>/', views.eliminar_empleado, name='eliminar_empleado'),
    path('todos_cargos/', views.todos_cargos, name='todos_cargos'),
    path('crear_cargo/', views.crear_cargo, name='crear_cargo'),
    path('cargar_editar_cargo/<int:id_cargo>/', views.cargar_editar_cargo, name='cargar_editar_cargo'),
    path('eliminar_cargo/<int:id_cargo>/', views.eliminar_cargo, name='eliminar_cargo'),
]
