from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth import login
import json
from django.utils import timezone
from django.contrib.auth.models import User, Group
from rrhh.models import Empleado, Cargo, AuthUser, Direccion
from django.db.models import Q
from .forms import EmpleadoForm, CargoForm, UsuarioForm, UsuarioEditarForm, DireccionForm, ContratoForm, LiquidacionForm
from .models import Empleado, Contrato, Jornada, Liquidacion
from .decorators import grupo_requerido


@grupo_requerido('rrhh','admin')
def inicio(request):
    return render(request, 'home.html')

@grupo_requerido('rrhh','admin')
def index(request):
    return render(request,'rrhh/index.html')

@grupo_requerido('rrhh','admin')
def gestor_rrhh(request):
    return render(request, 'templates_rrhh/gestor_rrhh.html')

@grupo_requerido('rrhh','admin')
def mantenedor_empleados(request):
    return render(request, 'templates_rrhh/mantenedor_empleados.html')

@grupo_requerido('rrhh','admin')
def mantenedor_contratos(request):
    return render(request, 'templates_rrhh/mantenedor_contratos.html')

@grupo_requerido('rrhh','admin')
def mantenedor_usuarios(request):
    return render(request, 'templates_rrhh/mantenedor_usuarios.html')

@grupo_requerido('rrhh','admin')
def mantenedor_contratos(request):
    return render(request, 'templates_rrhh/mantenedor_contratos.html')



#De aquí pa abajo las vistas de empleados
@login_required
@grupo_requerido('rrhh','admin')
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

@grupo_requerido('rrhh','admin')
def todos_empleados(request):
    # Obtener el parámetro de filtro de la URL, por defecto 'vigentes'
    filtro = request.GET.get('filtro', 'vigentes')
    query = request.GET.get('q', '') # Obtener el término de búsqueda para pasarlo al template

    if filtro == 'vigentes':
        empleados = Empleado.objects.filter(visible=True)
    elif filtro == 'eliminados':
        empleados = Empleado.objects.filter(visible=False)
    else: # 'todos' o cualquier otro valor
        empleados = Empleado.objects.all()
        
    data = {
        'empleados': empleados,
        'filtro': filtro,
        'query': query, # Pasamos el query para que el campo de búsqueda mantenga su valor
    }
    return render(request, 'templates_rrhh/empleado/todos_empleados.html', data)

@grupo_requerido('rrhh','admin')
def cargar_editar_empleado(request, id_empleado):
    empleado= get_object_or_404(Empleado,id=id_empleado)
    form = EmpleadoForm(instance=empleado)
    
    return render(request, 'templates_rrhh/empleado/editar_empleado.html', {'form': form, 'empleado': empleado})

@grupo_requerido('rrhh','admin')
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

@grupo_requerido('rrhh','admin')
def eliminar_empleado(request, id_empleado):
    empleado = get_object_or_404(Empleado, id=id_empleado)
    empleado.visible = False
    empleado.save()
    return redirect('todos_empleados')

@grupo_requerido('rrhh','admin')
def restaurar_empleado(request, id_empleado):
    empleado = get_object_or_404(Empleado, id=id_empleado)
    empleado.visible = True
    empleado.save()
    return redirect('todos_empleados')



#De aquú pa abajo las vistas de cargos
@grupo_requerido('rrhh','admin')
def crear_cargo(request):
    if request.method == 'POST':
        form = CargoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todos_cargos')
    else:
        form = CargoForm()
    
    return render(request, 'templates_rrhh/cargo/crear_cargo.html', {'form': form})

@grupo_requerido('rrhh','admin')
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

@grupo_requerido('rrhh','admin')
def cargar_editar_cargo(request, id_cargo):
    cargo= get_object_or_404(Cargo,id=id_cargo)
    form = CargoForm(instance=cargo)
    
    return render(request, 'templates_rrhh/cargo/editar_cargo.html', {'form': form, 'cargo': cargo})

@grupo_requerido('rrhh','admin')
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

@grupo_requerido('rrhh','admin')
def eliminar_cargo(request, id_cargo):
    cargo = get_object_or_404(Cargo, id=id_cargo)
    
    # Soft delete: en lugar de borrar, cambiamos el estado
    cargo.visible = False
    cargo.save()
    
    return redirect('todos_cargos')

@grupo_requerido('rrhh','admin')
def restaurar_cargo(request, id_cargo):
    cargo = get_object_or_404(Cargo, id=id_cargo)
    
    # Restaurar: cambiamos el estado a visible
    cargo.visible = True
    cargo.save()
    
    return redirect('todos_cargos')




#De aquí pa abajo las vistas de usuarios
@grupo_requerido('rrhh','admin')
def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            # Guardamos el usuario que devuelve el form.save()
            user = form.save()
            
            # Obtenemos el nombre del grupo seleccionado en el formulario
            group_name = form.cleaned_data.get('grupo')
            if group_name:
                # Buscamos el objeto Group y se lo asignamos al usuario
                group = Group.objects.get(name=group_name)
                user.groups.add(group)
            return redirect('todos_usuarios') # Redirigimos a la lista de usuarios
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

@grupo_requerido('rrhh','admin')
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


@grupo_requerido('rrhh','admin')
def editar_usuario(request, id_usuario):
    usuario = get_object_or_404(User, id=id_usuario)

    if request.method == 'POST':
        form = UsuarioEditarForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('todos_usuarios')
        else:print(form.errors)
    else:
        form = UsuarioEditarForm(instance=usuario)

    return render(request, 'templates_rrhh/usuario/editar_usuario.html', {'form': form, 'usuario': usuario})


@grupo_requerido('rrhh','admin')
def eliminar_usuario(request, id_usuario):
    usuario = get_object_or_404(AuthUser, id=id_usuario)
    # Soft delete: marcamos como no visible y desactivamos
    usuario.visible = False
    usuario.is_active = False
    usuario.save()
    return redirect('todos_usuarios')

@grupo_requerido('rrhh','admin')
def restaurar_usuario(request, id_usuario):
    usuario = get_object_or_404(AuthUser, id=id_usuario)
    usuario.visible = True
    usuario.save()
    return redirect('todos_usuarios')

@grupo_requerido('rrhh','admin')
def desactivar_usuario(request, id_usuario):
    usuario = get_object_or_404(AuthUser, id=id_usuario)
    usuario.is_active=0
    usuario.save()
    return redirect('todos_usuarios')

@grupo_requerido('rrhh','admin')
def activar_usuario(request, id_usuario):
    usuario = get_object_or_404(AuthUser, id=id_usuario)
    usuario.is_active=1
    usuario.save()
    return redirect('todos_usuarios')

# Vistas de contratos -----------------------------------------

@grupo_requerido('rrhh','admin')
def listar_contratos(request):
    # Obtener parámetros de la URL
    query = request.GET.get('q', '')
    filtro_vigencia = request.GET.get('filtro_vigencia', 'todos')
    filtro_visibilidad = request.GET.get('filtro_visibilidad', 'activos')
    user = request.user
    
    # Query base
    base_query = Contrato.objects.select_related('empleado', 'cargo', 'departamento').all()

    # Filtro por rol de usuario
    # Si el usuario no es superusuario, filtramos por su empleado asociado
    # a menos que sea del grupo rrhh o admin.
    if not user.is_superuser:
        # Un empleado normal solo puede ver su contrato.
        if not user.groups.filter(name__in=['rrhh', 'admin']).exists():
             base_query = base_query.filter(empleado__user=user)

    # Filtro por visibilidad (soft-delete)
    if filtro_visibilidad == 'eliminados':
        base_query = base_query.filter(visible=False)
    else: # 'activos'
        base_query = base_query.filter(visible=True)

    # Filtro por vigencia del contrato
    hoy = timezone.now().date()
    if filtro_vigencia == 'vigentes':
        base_query = base_query.filter(fecha_fin__gte=hoy)
    elif filtro_vigencia == 'vencidos':
        base_query = base_query.filter(fecha_fin__lt=hoy)
    # Si es 'todos', no se aplica filtro de vigencia.
    
    # Filtro por búsqueda de texto (nombre de empleado)
    if query:
        # Búsqueda más completa por nombre o apellidos
        base_query = base_query.filter(
            Q(empleado__nombres__icontains=query) |
            Q(empleado__a_paterno__icontains=query) |
            Q(empleado__a_materno__icontains=query))
    
    # Si la petición es AJAX, devolvemos los datos en formato JSON
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        contratos_data = list(base_query.values(
            'id',
            'empleado__nombres', 
            'empleado__a_paterno', 
            'empleado__a_materno',
            'cargo__nombre',
            'fecha_inicio',
            'fecha_fin',
            'sueldo_base'
        ))
        return JsonResponse({'contratos': contratos_data})

    # Si es una carga de página normal, renderizamos el HTML completo
    # Los datos se cargarán vía AJAX desde el frontend.
    # MODIFICACIÓN: Pasamos también los contratos en la carga inicial para que la tabla no aparezca vacía.
    context = {
        'contratos': base_query,
        'query': query, 
        'filtro_vigencia': filtro_vigencia, 
        'filtro_visibilidad': filtro_visibilidad
    }
    return render(request, 'templates_rrhh/contratos/listar_contratos.html', context)

@grupo_requerido('rrhh','admin')
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

@grupo_requerido('rrhh','admin')
def eliminar_contrato(request, contrato_id):
    contrato = get_object_or_404(Contrato, id=contrato_id)
    contrato.visible = False
    contrato.save()
    return redirect('listar_contratos')

@grupo_requerido('rrhh','admin')
def restaurar_contrato(request, contrato_id):
    contrato = get_object_or_404(Contrato, id=contrato_id)
    contrato.visible = True
    contrato.save()
    return redirect('listar_contratos')


# Vistas de liquidaciones ---------------------------------------

@grupo_requerido('rrhh','admin')
def listar_liquidaciones(request):
    # Obtener parámetros de la URL
    query = request.GET.get('q', '')
    filtro_visibilidad = request.GET.get('filtro_visibilidad', 'activos')
    user = request.user

    # Query base
    base_query = Liquidacion.objects.select_related('empleado').all()
    if filtro_visibilidad == 'eliminados':
        base_query = base_query.filter(visible=False)
    else: # 'activos'
        base_query = base_query.filter(visible=True)
    # Filtro por búsqueda de texto (nombre de empleado)
    if query:
        base_query = base_query.filter(empleado__nombres__icontains=query)

    # Filtro por rol de usuario
    # Un empleado normal solo puede ver su liquidación. RRHH y Admin ven todo.
    if not user.is_superuser and not user.groups.filter(name__in=['rrhh', 'admin']).exists():
        base_query = base_query.filter(empleado__user=user)


    # Si la petición es AJAX, devolvemos los datos en formato JSON
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        liquidaciones_data = list(base_query.values(
            'id', 
            'empleado__nombres', 
            'empleado__a_paterno', 
            'empleado__a_materno',
            'periodo', 
            'bruto', 
            'liquido'
        ))
        return JsonResponse({'liquidaciones': liquidaciones_data})

    # Pasamos también las liquidaciones en la carga inicial.
    context = {
        'liquidaciones': base_query,
        'query': query, 
        'filtro_visibilidad': filtro_visibilidad
    }
    return render(request, 'templates_rrhh/liquidaciones/listar_liquidaciones.html', context)

@grupo_requerido('rrhh','admin')
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

@grupo_requerido('rrhh','admin')
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

@grupo_requerido('rrhh','admin')
def eliminar_liquidacion(request, liquidacion_id):
    liquidacion = get_object_or_404(Liquidacion, id=liquidacion_id)
    liquidacion.visible = False
    liquidacion.save()
    return redirect("listar_liquidaciones")

@grupo_requerido('rrhh','admin')
def restaurar_liquidacion(request, liquidacion_id):
    liquidacion = get_object_or_404(Liquidacion, id=liquidacion_id)
    liquidacion.visible = True
    liquidacion.save()
    return redirect("listar_liquidaciones")
