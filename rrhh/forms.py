from django import forms
from .models import Cargo, Empleado, AuthUser, Direccion
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
import re

def validar_run(run):
    run = run.upper().strip()
    if not re.match(r'^\d{7,8}-[\dK]$', run):
        raise ValidationError("RUN inválido. Formato esperado: 12345678-5")

    cuerpo, dv = run.split('-')
    suma = 0
    multiplo = 2
    for c in reversed(cuerpo):
        suma += int(c) * multiplo
        multiplo = multiplo + 1 if multiplo < 7 else 2

    resto = suma % 11
    dv_esperado = '0' if resto == 0 else 'K' if resto == 1 else str(11 - resto)

    if dv != dv_esperado:
        raise ValidationError("RUN inválido: dígito verificador incorrecto.")




class DireccionForm(forms.ModelForm):
    class Meta:
        model = Direccion
        fields = ['calle', 'numero', 'depto', 'comuna', 'region', 'codigo_postal']


class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombres', 'a_paterno', 'a_materno', 'run', 'correo', 'fono']

    def clean_run(self):
        run = self.cleaned_data['run']
        validar_run(run)
        if Empleado.objects.filter(run__iexact=run).exclude(pk=self.instance.pk).exists():
            raise ValidationError("Este RUN ya está registrado.")
        return run



        
class CargoForm(forms.ModelForm):
    nombre=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese Nombre del Cargo'}))
    descripcion=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Ingrese Descripción del Cargo','rows':3}))
    
    class Meta:
        model = Cargo
        fields = {'nombre','descripcion'}


class UsuarioForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        error_messages={'invalid': 'Ingrese un correo con formato válido'}, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ej:Ingrese correo electrónico'}))

    email_confirmacion = forms.EmailField(
        required=True,
        error_messages={'invalid': 'Ingrese un correo con formato válido'}, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ej:Confirme correo electrónico'}))

    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','email_confirmacion','password1','password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).exclude(id=self.instance.id).exists():
            raise ValidationError("El correo electrónico ya está en uso.")
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username and User.objects.filter(username=username).exclude(id=self.instance.id).exists():
            raise ValidationError("El nombre de usuario ya está en uso.")
        return username

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        email = cleaned_data.get('email')
        email_confirmacion = cleaned_data.get('email_confirmacion')

        if email and email_confirmacion and email != email_confirmacion:
            self.add_error('email_confirmacion', "Los correos electrónicos no coinciden.")

        if not first_name:
            self.add_error('first_name', 'El nombre no puede estar vacío')

        if not last_name:
            self.add_error('last_name', 'Los apellidos no pueden estar vacío')

        return cleaned_data
    
class UsuarioEditarForm(forms.ModelForm):    
    
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email']
        