from django.contrib import admin

from rrhh.models import (Cargo, Contrato, CuentaBancaria, Departamento,
                         Direccion, Empleado, FormaPago, Jornada, Liquidacion,
                         Pago, Roles, Turno, TurnoHasJornada, Usuarios)

class CargoAdmin(admin.ModelAdmin):
    list_display = ['nombre','descripcion']
    
class ContratoAdmin(admin.ModelAdmin):
    list_display = ['detalle_contrato','fecha_inicio','fecha_fin','empleado','cargo', 'departamento']
    
class CuentaBancariaAdmin(admin.ModelAdmin):
    list_display = ['banco','tipo_cuenta','numero_cuenta','correo','empleado']
    
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ['nombre','descripcion']
    
class DireccionAdmin(admin.ModelAdmin):
    list_display = ['calle','numero','depto','comuna','region','codigo_postal']
    
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ['nombres','a_paterno','a_materno','run','correo','fono','nacionalidad']
    
class FormaPagoAdmin(admin.ModelAdmin):
    list_display = ['nombre','descripcion','pago']
    
class JornadaAdmin(admin.ModelAdmin):
    list_display = ['nombre','horas_semanales']
    
class LiquidacionAdmin(admin.ModelAdmin):
    list_display = ['periodo','imponible','no_imponible','descuentos','bruto','liquido','fecha_cierre','estado','contrato']
    
class PagoAdmin(admin.ModelAdmin):
    list_display = ['fecha_pago','monto','comprobante','estado','liquidacion']
    
class RolesAdmin(admin.ModelAdmin):
    list_display = ['nombre','descripcion']

class TurnoAdmin(admin.ModelAdmin):
    list_display = ['hora_entrada','hora_salida']
    
class TurnoHasJornadaAdmin(admin.ModelAdmin):
    list_display = ['turno','jornada']
    
class UsuariosAdmin(admin.ModelAdmin):
    list_display = ['nombres','paterno','materno','run','correo','fono','clave','direccion','roles']
    
admin.site.register(Cargo, CargoAdmin)
admin.site.register(Contrato, ContratoAdmin) 
admin.site.register(CuentaBancaria, CuentaBancariaAdmin)
admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Direccion, DireccionAdmin)
admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(FormaPago, FormaPagoAdmin)
admin.site.register(Jornada, JornadaAdmin)
admin.site.register(Liquidacion, LiquidacionAdmin)
admin.site.register(Pago, PagoAdmin)
admin.site.register(Roles, RolesAdmin)
admin.site.register(Turno, TurnoAdmin)
admin.site.register(TurnoHasJornada, TurnoHasJornadaAdmin)
admin.site.register(Usuarios, UsuariosAdmin)