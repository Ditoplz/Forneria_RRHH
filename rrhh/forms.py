from django import forms
from .models import Cargo, Empleado, AuthUser, Direccion, Contrato, Liquidacion
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
        widgets = {
            'calle': forms.TextInput(attrs={'class': 'form-control'}),
            'numero': forms.TextInput(attrs={'class': 'form-control'}),
            'depto': forms.TextInput(attrs={'class': 'form-control'}),
            'comuna': forms.TextInput(attrs={'class': 'form-control'}),
            'region': forms.Select(attrs={'class': 'form-select'}),
            'codigo_postal': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombres', 'a_paterno', 'a_materno', 'run', 'correo', 'fono']
        widgets = {
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'a_paterno': forms.TextInput(attrs={'class': 'form-control'}),
            'a_materno': forms.TextInput(attrs={'class': 'form-control'}),
            'run': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'fono': forms.TextInput(attrs={'class': 'form-control'}),
        }

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


class UsuarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}), label="Contraseña")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmar contraseña'}), label="Confirmar contraseña")
    
    empleado = forms.ModelChoiceField(
        queryset=Empleado.objects.filter(user__isnull=True),
        required=False,
        label="Opcional: Vincular a un empleado existente",
        widget=forms.Select(attrs={'class': 'form-select'}),
        help_text="Si seleccionas un empleado, sus datos se cargarán automáticamente."
    )

    username = forms.CharField(
        label="Nombre de usuario",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario'}),
        help_text=""  # Esto elimina el texto de ayuda
    )

    class Meta:
        model = User
        fields = ['empleado', 'username', 'first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombres'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellidos'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'}),
        }

    def __init__(self, *args, **kwargs):
        super(UsuarioForm, self).__init__(*args, **kwargs)
        # Definir y aplicar el orden deseado para los campos del formulario
        self.order_fields([
            'empleado', 
            'username', 
            'first_name', 
            'last_name', 
            'email', 
            'password', 
            'password2'
        ])

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if first_name and not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', first_name):
            raise ValidationError("El nombre solo debe contener letras y espacios.")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if last_name and not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', last_name):
            raise ValidationError("El apellido solo debe contener letras y espacios.")
        return last_name

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username__iexact=username).exists():
            raise ValidationError("Este nombre de usuario ya está en uso. Por favor, elige otro.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email__iexact=email).exists():
            raise ValidationError("Este correo electrónico ya está registrado. Por favor, usa otro.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")
        empleado = cleaned_data.get('empleado')
        username = cleaned_data.get('username')

        if not username:
            self.add_error('username', "El nombre de usuario es obligatorio.")

        if password and password2 and password != password2:
            self.add_error('password2', "Las contraseñas no coinciden.")

        # Validación de complejidad de la contraseña
        if password:
            if len(password) < 8:
                self.add_error('password', "La contraseña debe tener al menos 8 caracteres.")
            if not re.search(r'[A-Z]', password):
                self.add_error('password', "La contraseña debe contener al menos una letra mayúscula.")
            if not re.search(r'[a-z]', password):
                self.add_error('password', "La contraseña debe contener al menos una letra minúscula.")
            if not re.search(r'[0-9]', password):
                self.add_error('password', "La contraseña debe contener al menos un número.")

        # Si no se selecciona un empleado, los campos de nombre, apellido y email son obligatorios
        if not empleado:
            if not cleaned_data.get('first_name'):
                self.add_error('first_name', 'Este campo es obligatorio si no se crea desde un empleado.')
            if not cleaned_data.get('last_name'):
                self.add_error('last_name', 'Este campo es obligatorio si no se crea desde un empleado.')
            if not cleaned_data.get('email'):
                self.add_error('email', 'El correo es obligatorio si no se crea desde un empleado.')

        return cleaned_data

    def save(self, commit=True):
        # Creamos el usuario pero no lo guardamos aún para poder asignar la contraseña
        user = super(UsuarioForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        
        empleado = self.cleaned_data.get('empleado')
        
        if empleado:
            # Si se seleccionó un empleado, llenamos los datos del usuario
            user.first_name = empleado.nombres
            user.last_name = f"{empleado.a_paterno} {empleado.a_materno}"
            user.email = empleado.correo
        
        if commit:
            user.save()
            if empleado:
                # Una vez guardado el usuario, lo asociamos al empleado
                empleado.user = user
                empleado.save()

        return user
    
class UsuarioEditarForm(forms.ModelForm):    
    
    class Meta:
        model = AuthUser
        fields = ['first_name','last_name','username','email']
        

class ContratoForm(forms.ModelForm):
    class Meta:
        model = Contrato
        fields = [
            "empleado",
            "cargo",
            "departamento",
            "turno_has_jornada",
            "sueldo_base",
            "detalle_contrato",
            "fecha_inicio",
            "fecha_fin",
        ]

        widgets = {
            "fecha_inicio": forms.DateInput(attrs={"type": "date"}),
            "fecha_fin": forms.DateInput(attrs={"type": "date"}),
            "sueldo_base": forms.NumberInput(attrs={"min": 0}),
            "detalle_contrato": forms.TextInput(),
        }


class LiquidacionForm(forms.ModelForm):

    class Meta:
        model = Liquidacion
        fields = [
            "contrato",
            "periodo",
            "imponible",
            "no_imponible",
            "tributable",
            "descuentos",
            "bruto",
            "liquido",
            "fecha_cierre",
            "estado",
        ]
        widgets = {
            "periodo": forms.DateInput(attrs={"type": "date"}),
            "fecha_cierre": forms.DateInput(attrs={"type": "date"}),
        }

    def __init__(self, *args, **kwargs):
        empleado_id = kwargs.pop("empleado_id", None)
        super().__init__(*args, **kwargs)

        if empleado_id:
            self.fields["contrato"].queryset = Contrato.objects.filter(empleado_id=empleado_id)
        else:
            self.fields["contrato"].queryset = Contrato.objects.none()
