from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
import json
from django.contrib.auth.models import User # Se mantiene para el formulario de creación
from rrhh.models import Empleado, Cargo, AuthUser, Direccion
from django.db.models import Q
from .forms import EmpleadoForm, CargoForm, UsuarioForm, UsuarioEditarForm, DireccionForm, ContratoForm, LiquidacionForm
from .models import Empleado, Contrato, Jornada, Liquidacion

@login_required
def inicio(request):
    return render(request, 'home.html')

@login_required
def index(request):
    return render(request,'rrhh/index.html')

@login_required
def gestor_rrhh(request):
    return render(request, 'templates_rrhh/gestor_rrhh.html')

@login_required
def mantenedor_empleados(request):
    return render(request, 'templates_rrhh/mantenedor_empleados.html')

@login_required
def mantenedor_contratos(request):
    return render(request, 'templates_rrhh/mantenedor_contratos.html')

@login_required
def mantenedor_usuarios(request):
    return render(request, 'templates_rrhh/mantenedor_usuarios.html')

@login_required
def mantenedor_contratos(request):
    return render(request, 'templates_rrhh/mantenedor_contratos.html')



#De aquí pa abajo las vistas de empleados
@login_required
def crear_empleado(request):
    if request.method == 'POST':
        empleado_form = EmpleadoForm(request.POST)
        direccion_form = DireccionForm(request.POST)
        if empleado_form.is_valid() and direccion_form.is_valid():
            direccion = direccion_form.save()
            empleado = empleado_form.save(commit=False)
            empleado.id_direccion = direccion.id
            empleado.save()
            return redirect('todos_empleados')
    else:
        empleado_form = EmpleadoForm()
        direccion_form = DireccionForm()
    return render(request, 'templates_rrhh/empleado/crear_empleado.html', {
        'empleado_form': empleado_form,
        'direccion_form': direccion_form
    })


def todos_empleados(request):
    estado = request.GET.get('estado', 'activos')

    if estado == 'eliminados':
        empleados = Empleado.objects.filter(visible=False)
    else:
        empleados = Empleado.objects.filter(visible=True)
        
    data = {
        'empleados': empleados,
        'estado': estado
    }
    return render(request, 'templates_rrhh/empleado/todos_empleados.html', data)

def cargar_editar_empleado(request, id_empleado):
    empleado= get_object_or_404(Empleado,id=id_empleado)
    form = EmpleadoForm(instance=empleado)
    
    return render(request, 'templates_rrhh/empleado/editar_empleado.html', {'form': form, 'empleado': empleado})

@login_required
def editar_empleado(request, id_empleado):
    empleado = get_object_or_404(Empleado, id=id_empleado)
    direccion = get_object_or_404(Direccion, id=empleado.id_direccion)

    if request.method == 'POST':
        empleado_form = EmpleadoForm(request.POST, instance=empleado)
        direccion_form = DireccionForm(request.POST, instance=direccion)
        if empleado_form.is_valid() and direccion_form.is_valid():
            direccion_form.save()
            empleado_form.save()
            return redirect('todos_empleados')
    else:
        empleado_form = EmpleadoForm(instance=empleado)
        direccion_form = DireccionForm(instance=direccion)

    return render(request, 'templates_rrhh/empleado/editar_empleado.html', {
        'empleado_form': empleado_form,
        'direccion_form': direccion_form,
        'empleado': empleado
    })

@login_required
def eliminar_empleado(request, id_empleado):
    empleado = get_object_or_404(Empleado, id=id_empleado)
    empleado.visible = False
    empleado.save()
    return redirect('todos_empleados')

@login_required
def restaurar_empleado(request, id_empleado):
    empleado = get_object_or_404(Empleado, id=id_empleado)
    empleado.visible = True
    empleado.save()
    return redirect('todos_empleados')



#De aquú pa abajo las vistas de cargos
@login_required
def crear_cargo(request):
    if request.method == 'POST':
        form = CargoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todos_cargos')
    else:
        form = CargoForm()
    
    return render(request, 'templates_rrhh/cargo/crear_cargo.html', {'form': form})

def todos_cargos(request):
    filtro = request.GET.get('filtro', 'vigentes')
    query = request.GET.get('q', '') # Obtener el término de búsqueda

    if filtro == 'eliminados':
        base_queryset = Cargo.objects.filter(visible=False)
    elif filtro == 'todos':
        base_queryset = Cargo.objects.all()
    else:
        # Por defecto, muestra solo los vigentes
        base_queryset = Cargo.objects.filter(visible=True)

    if query:
        # Aplicar el filtro de búsqueda si existe
        base_queryset = base_queryset.filter(Q(nombre__icontains=query) | Q(descripcion__icontains=query))
        
    data = {
        'cargos': base_queryset,
        'filtro': filtro,
        'query': query # Pasar el query a la plantilla para mantenerlo en la barra de búsqueda
    }
    return render(request, 'templates_rrhh/cargo/todos_cargos.html', data)

def cargar_editar_cargo(request, id_cargo):
    cargo= get_object_or_404(Cargo,id=id_cargo)
    form = CargoForm(instance=cargo)
    
    return render(request, 'templates_rrhh/cargo/editar_cargo.html', {'form': form, 'cargo': cargo})

def editar_cargo(request, id_cargo):
    cargo= get_object_or_404(Cargo,id=id_cargo)
    
    if request.method == 'POST':
        form = CargoForm(request.POST, instance=cargo)
        if form.is_valid():
            form.save()
            return redirect('todos_cargos')
    else:
        form = CargoForm(instance=cargo)
    
    return render(request, 'templates_rrhh/cargo/editar_cargo.html', {'form': form, 'cargo': cargo})

def eliminar_cargo(request, id_cargo):
    cargo = get_object_or_404(Cargo, id=id_cargo)
    
    # Soft delete: en lugar de borrar, cambiamos el estado
    cargo.visible = False
    cargo.save()
    
    return redirect('todos_cargos')

def restaurar_cargo(request, id_cargo):
    cargo = get_object_or_404(Cargo, id=id_cargo)
    
    # Restaurar: cambiamos el estado a visible
    cargo.visible = True
    cargo.save()
    
    return redirect('todos_cargos')




#De aquí pa abajo las vistas de usuarios
@login_required
def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            # Podrías añadir un mensaje de éxito aquí si quieres
            return redirect('todos_usuarios')
    else:
        form = UsuarioForm()

    # Preparamos los datos de los empleados para el JavaScript del frontend
    # Esto nos permitirá autocompletar el formulario sin hacer más llamadas al servidor
    empleados_sin_cuenta = Empleado.objects.filter(user__isnull=True)
    empleados_data = {
        emp.id: {
            'nombres': emp.nombres,
            'apellidos': f'{emp.a_paterno} {emp.a_materno}'.strip(),
            'email': emp.correo
        } for emp in empleados_sin_cuenta
    }

    context = {
        'form': form,
        'empleados_data': json.dumps(empleados_data)
    }
    return render(request, 'templates_rrhh/usuario/crear_usuario.html', context)

@login_required
def todos_usuarios(request):
    filtro = request.GET.get('filtro', 'vigentes')

    if filtro == 'eliminados':
        usuarios = AuthUser.objects.filter(visible=False)
    elif filtro == 'todos':
        usuarios = AuthUser.objects.all()
    else:
        # Por defecto, muestra solo los vigentes (visible=True)
        usuarios = AuthUser.objects.filter(visible=True)
        
    data = {
        'usuarios': usuarios,
        'filtro': filtro
    }
    return render(request, 'templates_rrhh/usuario/todos_usuarios.html', data)


@login_required
def editar_usuario(request, id_usuario):
    usuario = get_object_or_404(AuthUser, id=id_usuario)

    if request.method == 'POST':
        form = UsuarioEditarForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('todos_usuarios')
        else:print(form.errors)
    else:
        form = UsuarioEditarForm(instance=usuario)

    return render(request, 'templates_rrhh/usuario/editar_usuario.html', {'form': form, 'usuario': usuario})


@login_required
def eliminar_usuario(request, id_usuario):
    usuario = get_object_or_404(AuthUser, id=id_usuario)
    # Soft delete: marcamos como no visible y desactivamos
    usuario.visible = False
    usuario.is_active = False
    usuario.save()
    return redirect('todos_usuarios')

@login_required
def restaurar_usuario(request, id_usuario):
    usuario = get_object_or_404(AuthUser, id=id_usuario)
    usuario.visible = True
    usuario.save()
    return redirect('todos_usuarios')

@login_required
def desactivar_usuario(request, id_usuario):
    usuario = get_object_or_404(AuthUser, id=id_usuario)
    usuario.is_active=0
    usuario.save()
    return redirect('todos_usuarios')

@login_required
def activar_usuario(request, id_usuario):
    usuario = get_object_or_404(AuthUser, id=id_usuario)
    usuario.is_active=1
    usuario.save()
    return redirect('todos_usuarios')

# Vistas de contratos -----------------------------------------
def listar_contratos(request):
    estado = request.GET.get('estado', 'activos')
    user = request.user

    if estado == 'eliminados':
        base_query = Contrato.objects.filter(visible=False)
    else:
        base_query = Contrato.objects.filter(visible=True)

    if not user.is_superuser:
        base_query = base_query.filter(empleado__user=user)

    return render(request, 'templates_rrhh/contratos/listar_contratos.html', {'contratos': base_query, 'estado': estado})

def crear_contrato(request):
    if request.method == 'POST':
        form = ContratoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_contratos')
    else:
        form = ContratoForm()
    return render(request, 'templates_rrhh/contratos/crear_contrato.html', {'form': form})

def editar_contrato(request, contrato_id):
    contrato = get_object_or_404(Contrato, id=contrato_id)
    if request.method == 'POST':
        form = ContratoForm(request.POST, instance=contrato)
        if form.is_valid():
            form.save()
            return redirect('listar_contratos')
    else:
        form = ContratoForm(instance=contrato)
    return render(request, 'templates_rrhh/contratos/editar_contrato.html', {'form': form})

def eliminar_contrato(request, contrato_id):
    contrato = get_object_or_404(Contrato, id=contrato_id)
    contrato.visible = False
    contrato.save()
    return redirect('listar_contratos')

def restaurar_contrato(request, contrato_id):
    contrato = get_object_or_404(Contrato, id=contrato_id)
    contrato.visible = True
    contrato.save()
    return redirect('listar_contratos')


# Vistas de liquidaciones ---------------------------------------

def listar_liquidaciones(request):
    estado = request.GET.get('estado', 'activos')
    user = request.user

    if estado == 'eliminados':
        base_query = Liquidacion.objects.filter(visible=False)
    else:
        base_query = Liquidacion.objects.filter(visible=True)

    if not user.is_superuser:
        base_query = base_query.filter(empleado__user=user)

    return render(request, 'templates_rrhh/liquidaciones/listar_liquidaciones.html', {'liquidaciones': base_query, 'estado': estado})

def crear_liquidacion(request):
    empleado_id = request.GET.get("empleado")

    # Para rellenar el select del primer formulario
    empleados = Empleado.objects.all()

    if request.method == "POST":
        # Recuperamos el empleado elegido previamente
        empleado_id = request.POST.get("empleado_id")

        data = request.POST.copy()
        data["empleado"] = empleado_id  # <<--- esto es CLAVE

        form = LiquidacionForm(data, empleado_id=empleado_id)

        if form.is_valid():
            form.save()
            return redirect("listar_liquidaciones")
        else:
            print("ERRORES FORM:", form.errors)  # revisa tu consola
    else:
        form = LiquidacionForm(empleado_id=empleado_id)

    data = {
        "form": form,
        "empleados": empleados,
        "empleado_id": empleado_id,
    }

    return render(
        request,
        "templates_rrhh/liquidaciones/crear_liquidacion.html",
        data
    )

def editar_liquidacion(request, id):
    liquidacion = get_object_or_404(Liquidacion, id=id)

    if request.method == "POST":
        form = LiquidacionForm(request.POST, instance=liquidacion, empleado_id=liquidacion.empleado.id)
        if form.is_valid():
            form.save()
            return redirect("listar_liquidaciones")
    else:
        form = LiquidacionForm(instance=liquidacion, empleado_id=liquidacion.empleado.id)

    return render(
        request,
        "templates_rrhh/liquidaciones/editar_liquidacion.html",
        {"form": form, "liquidacion": liquidacion}
    )


def eliminar_liquidacion(request, liquidacion_id):
    liquidacion = get_object_or_404(Liquidacion, id=liquidacion_id)
    liquidacion.visible = False
    liquidacion.save()
    return redirect("listar_liquidaciones")

def restaurar_liquidacion(request, liquidacion_id):
    liquidacion = get_object_or_404(Liquidacion, id=liquidacion_id)
    liquidacion.visible = True
    liquidacion.save()
    return redirect("listar_liquidaciones")
