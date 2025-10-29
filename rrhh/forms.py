from django import forms
from .models import Cargo, Clientes, Contrato, CuentaBancaria, Departamento, Direccion, Empleado, FormaPago, Jornada, Liquidacion, Pago, Roles, Turno, TurnoHasJornada, Usuarios


class EmpleadoForm(forms.ModelForm):
    nombres=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese Nombre(s)'}))
    a_paterno=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese Apellido Paterno'}))
    a_materno=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese Apellido Materno'}))
    run=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'12345678-9'}))
    correo=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Ej: usuario@dominio.com'}))
    fono=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ej: +56912345678'}))
    nacionalidad=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese Nacionalidad'}))
    
    class Meta:
        model = Empleado
        fields = '__all__'