import re
from django.db import models
from django.forms import ValidationError
from django.contrib.auth.models import User


class Alertas(models.Model):
    tipo_alerta = models.CharField(max_length=8)
    mensaje = models.CharField(max_length=255)
    fecha_generada = models.DateTimeField(blank=True, null=True)
    estado = models.CharField(max_length=20, blank=True, null=True)
    productos = models.ForeignKey('Productos', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'alertas'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField(blank=True, null=True)
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(unique=True, max_length=254)
    is_staff = models.IntegerField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    date_joined = models.DateTimeField(blank=True, null=True)
    visible = models.BooleanField(default=True)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class Cargo(models.Model):
    nombre = models.CharField(max_length=45, unique=True)
    descripcion = models.CharField(max_length=300, blank=True)
    visible = models.BooleanField(default=True)

    class Meta:
        managed = False
        db_table = 'cargo'
        
    def __str__(self):
        return self.nombre


class Categorias(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categorias'

    def __str__(self):
        return self.nombre



class Clientes(models.Model):
    rut = models.CharField(max_length=12, blank=True, null=True)
    nombre = models.CharField(max_length=150)
    correo = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clientes'

    def __str__(self):
        return self.nombre


class Contrato(models.Model):
    detalle_contrato = models.CharField(max_length=45)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    empleado = models.ForeignKey('Empleado', models.DO_NOTHING)
    cargo = models.ForeignKey(Cargo, models.DO_NOTHING)
    departamento = models.ForeignKey('Departamento', models.DO_NOTHING)
    turno_has_jornada = models.ForeignKey('TurnoHasJornada', models.DO_NOTHING)

    sueldo_base = models.IntegerField()
    visible = models.BooleanField(default=True)

    @property
    def jornada(self):
        from .models import Jornada
        try:
            return Jornada.objects.get(id=self.turno_has_jornada.jornada_id)
        except Jornada.DoesNotExist:
            return None

    @property
    def horas_semanales(self):
        return self.jornada.horas_semanales if self.jornada else None

    class Meta:
        managed = False
        db_table = 'contrato'

    def __str__(self):
        return f"Contrato {self.id} - {self.empleado}"


class CuentaBancaria(models.Model):
    banco = models.CharField(max_length=45)
    tipo_cuenta = models.CharField(max_length=45)
    numero_cuenta = models.IntegerField()
    correo = models.CharField(max_length=45)
    empleado = models.ForeignKey('Empleado', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cuenta_bancaria'

    def __str__(self):
        return f"{self.banco} - {self.numero_cuenta}"


class Departamento(models.Model):
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'departamento'

    def __str__(self):
        return self.nombre



class DetalleVenta(models.Model):
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    descuento_pct = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    ventas = models.ForeignKey('Ventas', models.DO_NOTHING)
    productos = models.ForeignKey('Productos', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'detalle_venta'


REGIONES = [
    ('XV - Arica y Parinacota', 'XV - Arica y Parinacota'),
    ('I - Tarapacá', 'I - Tarapacá'),
    ('II - Antofagasta', 'II - Antofagasta'),
    ('III - Atacama', 'III - Atacama'),
    ('IV - Coquimbo', 'IV - Coquimbo'),
    ('V - Valparaíso', 'V - Valparaíso'),
    ('RM - Metropolitana de Santiago', 'RM - Metropolitana de Santiago'),
    ('VI - O’Higgins', 'VI - O’Higgins'),
    ('VII - Maule', 'VII - Maule'),
    ('VIII - Biobío', 'VIII - Biobío'),
    ('IX - La Araucanía', 'IX - La Araucanía'),
    ('X - Los Lagos', 'X - Los Lagos'),
    ('XI - Aysén', 'XI - Aysén'),
    ('XII - Magallanes', 'XII - Magallanes'),
    ('XIV - Los Ríos', 'XIV - Los Ríos'),
    ('XIII - Ñuble', 'XIII - Ñuble'),
]

class Direccion(models.Model):
    calle = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    depto = models.CharField(max_length=10, blank=True, null=True)
    comuna = models.CharField(max_length=100)
    region = models.CharField(max_length=100, choices=REGIONES)
    codigo_postal = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'direccion'

    def __str__(self):
        return f"{self.calle} {self.numero}, {self.comuna}"



class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Empleado(models.Model):
    nombres = models.CharField(max_length=100)
    a_paterno = models.CharField(db_column='A_paterno', max_length=45)  # Field name made lowercase.
    a_materno = models.CharField(db_column='A_materno', max_length=45)  # Field name made lowercase.
    run = models.CharField(unique=True, max_length=45)
    correo = models.EmailField(max_length=100, unique=True)
    fono = models.CharField(unique=True, max_length=100)
    id_direccion = models.IntegerField(unique=True, null=False)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='empleado')
    visible = models.BooleanField(default=True)
    #direccion= models.ForeignKey('Direccion',to_field='id',db_column='id_direccion',on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'empleado'
        
    def clean_correo(self):
        correo = self.cleaned_data['correo']
        if Empleado.objects.filter(correo=correo).exists():
            raise ValidationError("Este correo ya está registrado.")
        return correo
    
    def clean_fono(self):
        fono = self.cleaned_data['fono']
        if not re.match(r'^\d{9}$', str(fono)):
            raise ValidationError("El número debe tener 9 dígitos.")
        return fono
    
    def __str__(self):
        return f"{self.nombres} {self.a_paterno} {self.a_materno}"


class FormaPago(models.Model):
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45)
    pago = models.ForeignKey('Pago', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'forma_pago'

    def __str__(self):
        return self.nombre


class Jornada(models.Model):
    nombre = models.CharField(max_length=45)
    horas_semanales = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jornada'

    def __str__(self):
        return f"{self.nombre} - {self.horas_semanales} hrs"



class Liquidacion(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE)
    
    periodo = models.DateField()
    imponible = models.IntegerField()
    no_imponible = models.IntegerField()
    tributable = models.IntegerField()
    descuentos = models.IntegerField()
    bruto = models.IntegerField()
    liquido = models.IntegerField()
    fecha_cierre = models.DateField()
    estado = models.CharField(max_length=45)
    visible = models.BooleanField(default=True)

    class Meta:
        db_table = 'liquidacion'

    def __str__(self):
        return f"Liquidación {self.id} - {self.empleado}"


class MovimientosInventario(models.Model):
    tipo_movimiento = models.CharField(max_length=7)
    cantidad = models.IntegerField()
    fecha = models.DateTimeField()
    productos = models.ForeignKey('Productos', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'movimientos_inventario'

    def __str__(self):
        return f"{self.tipo_movimiento} - {self.cantidad}"



class Nutricional(models.Model):
    ingredientes = models.CharField(max_length=300, blank=True, null=True)
    tiempo_preparacion = models.CharField(max_length=100, blank=True, null=True)
    proteinas = models.CharField(max_length=45, blank=True, null=True)
    azucar = models.CharField(max_length=45, blank=True, null=True)
    gluten = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nutricional'

    def __str__(self):
        return f"Nutricional {self.id}"


class Pago(models.Model):
    fecha_pago = models.DateField()
    monto = models.IntegerField()
    comprobante = models.CharField(max_length=45)
    estado = models.CharField(max_length=45)
    liquidacion_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pago'

    def __str__(self):
        return f"Pago {self.id} - {self.estado}"


class Productos(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300, blank=True, null=True)
    marca = models.CharField(max_length=100, blank=True, null=True)
    precio = models.IntegerField(blank=True, null=True)
    caducidad = models.DateField()
    elaboracion = models.DateField(blank=True, null=True)
    tipo = models.CharField(max_length=100, db_comment='Corresponde al tipo de elaboraci¾n, por ejemplo propia o envasado.')
    categorias_id = models.IntegerField(db_column='Categorias_id')  # Field name made lowercase.
    stock_actual = models.IntegerField(blank=True, null=True)
    stock_minimo = models.IntegerField(blank=True, null=True)
    stock_maximo = models.IntegerField(blank=True, null=True)
    presentacion = models.CharField(max_length=100, blank=True, null=True, db_comment='Unidad con la que se almacena el producto')
    formato = models.CharField(max_length=100, blank=True, null=True, db_comment='Cantidad de unidades o detalle por presentaci¾n')
    nutricional_id = models.IntegerField(db_column='Nutricional_id')  # Field name made lowercase.
    creado = models.DateTimeField(blank=True, null=True)
    modificado = models.DateTimeField(blank=True, null=True)
    eliminado = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'productos'

    def __str__(self):
        return self.nombre


class Turno(models.Model):
    hora_entrada = models.TimeField()
    hora_salida = models.TimeField()

    class Meta:
        managed = False
        db_table = 'turno'

    def __str__(self):
        return f"{self.hora_entrada} - {self.hora_salida}"


class TurnoHasJornada(models.Model):
    turno_id = models.IntegerField()
    jornada_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'turno_has_jornada'

    def __str__(self):
        return f"Turno {self.turno_id} - Jornada {self.jornada_id}"


class Ventas(models.Model):
    fecha = models.DateTimeField()
    total_sin_iva = models.DecimalField(max_digits=10, decimal_places=2)
    total_iva = models.DecimalField(max_digits=10, decimal_places=2)
    descuento = models.DecimalField(max_digits=10, decimal_places=2)
    total_con_iva = models.DecimalField(max_digits=10, decimal_places=2)
    canal_venta = models.CharField(max_length=10)
    folio = models.CharField(max_length=20, blank=True, null=True)
    monto_pagado = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    vuelto = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    clientes_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ventas'

    def __str__(self):
        return f"Venta {self.id} - {self.fecha}"
