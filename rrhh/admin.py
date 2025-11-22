from django.contrib import admin

from rrhh.models import (Cargo, Contrato, CuentaBancaria, Departamento,
                         Direccion, Empleado, FormaPago, Jornada, Liquidacion,
                         Pago, Turno, TurnoHasJornada)

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
    
class FormaPagoAdmin(admin.ModelAdmin):
    list_display = ['nombre','descripcion','pago']
    
class JornadaAdmin(admin.ModelAdmin):
    list_display = ['nombre','horas_semanales']
    
    
admin.site.register(Cargo, CargoAdmin)
admin.site.register(Contrato, ContratoAdmin) 
admin.site.register(CuentaBancaria, CuentaBancariaAdmin)
admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Direccion, DireccionAdmin)
admin.site.register(FormaPago, FormaPagoAdmin)
admin.site.register(Jornada, JornadaAdmin)