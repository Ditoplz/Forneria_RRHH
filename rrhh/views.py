from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.models import User
from rrhh.models import Empleado, Cargo, AuthUser, Direccion
from .forms import EmpleadoForm, CargoForm, UsuarioForm, UsuarioEditarForm, DireccionForm

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
    empleados=Empleado.objects.all()
    
    data={
        'empleados':empleados
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
    if request.method == 'POST':
        empleado.delete()
        return redirect('todos_empleados')
    return render(request, 'templates_rrhh/empleado/eliminar_empleado.html', {
        'empleado': empleado
    })



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
    cargos=Cargo.objects.all() 
    data={
        'cargos':cargos
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
    
    if request.method == 'POST':
        cargo.delete()
        return redirect('todos_cargos')
    
    return render(request, 'templates_rrhh/cargo/eliminar_cargo.html', {'cargo': cargo})


#De aquí pa abajo las vistas de usuarios
@login_required
def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.is_active = True
            usuario.save()
            return redirect('todos_usuarios')
        
    else:
        form = UsuarioForm()
    return render(request, 'templates_rrhh/usuario/crear_usuario.html', {'form': form})

@login_required
def todos_usuarios(request):
    usuarios = AuthUser.objects.all()
    return render(request, 'templates_rrhh/usuario/todos_usuarios.html', {'usuarios': usuarios})


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
    if request.method == 'POST':
        usuario.delete()
        return redirect('todos_usuarios')
    return render(request, 'templates_rrhh/usuario/eliminar_usuario.html', {
        'usuario': usuario
    })

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