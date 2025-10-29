from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from rrhh.models import Empleado, Cargo, Usuarios
from .forms import EmpleadoForm, CargoForm, UsuarioForm

@login_required
def index(request):
    return render(request,'rrhh/index.html')

@login_required
def gestor_rrhh(request):
    return render(request, 'gestor_rrhh.html')

@login_required
def mantenedor_empleados(request):
    return render(request, 'mantenedor_empleados.html')

@login_required
def mantenedor_contratos(request):
    return render(request, 'mantenedor_contratos.html')

@login_required
def mantenedor_usuarios(request):
    return render(request, 'mantenedor_usuarios.html')


#De aquí pa abajo las vistas de empleados
@login_required
def crear_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todos_empleados')
    else:
        form = EmpleadoForm()
    
    return render(request, 'crear_empleado.html', {'form': form})

def todos_empleados(request):
    empleados=Empleado.objects.all()
    
    data={
        'empleados':empleados
    }
    
    return render(request, 'todos_empleados.html', data)

def cargar_editar_empleado(request, id_empleado):
    empleado= get_object_or_404(Empleado,id=id_empleado)
    form = EmpleadoForm(instance=empleado)
    
    return render(request, 'editar_empleado.html', {'form': form, 'empleado': empleado})

def editar_empleado(request, id_empleado):
    empleado= get_object_or_404(Empleado,id=id_empleado)
    
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('todos_empleados')
    
    return render(request, 'editar_empleado.html', {'form': form, 'empleado': empleado})

def eliminar_empleado(request, id_empleado):
    empleado = get_object_or_404(Empleado, id=id_empleado)
    
    if request.method == 'POST':
        empleado.delete()
        return redirect('todos_empleados')
    return render(request, 'templates_rrhh/eliminar_empleado.html', {'empleado': empleado})


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
    
    return render(request, 'crear_cargo.html', {'form': form})

def todos_cargos(request):
    cargos=Cargo.objects.all()
    
    data={
        'cargos':cargos
    }
    
    return render(request, 'todos_cargos.html', data)

def cargar_editar_cargo(request, id_cargo):
    cargo= get_object_or_404(Cargo,id=id_cargo)
    form = CargoForm(instance=cargo)
    
    return render(request, 'editar_cargo.html', {'form': form, 'cargo': cargo})

def editar_cargo(request, id_cargo):
    cargo= get_object_or_404(Cargo,id=id_cargo)
    
    if request.method == 'POST':
        form = CargoForm(request.POST, instance=cargo)
        if form.is_valid():
            form.save()
            return redirect('todos_cargos')
    
    return render(request, 'editar_cargo.html', {'form': form, 'cargo': cargo})

def eliminar_cargo(request, id_cargo):
    cargo = get_object_or_404(Cargo, id=id_cargo)
    
    if request.method == 'POST':
        cargo.delete()
        return redirect('todos_cargos')
    
    return render(request, 'templates_rrhh/eliminar_cargo.html', {'cargo': cargo})


#De aquí pa abajo las vistas de usuarios
@login_required
def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todos_usuarios')
    else:
        form = UsuarioForm()
    
    return render(request, 'crear_usuario.html', {'form': form})

def todos_usuarios(request):
    usuarios=Usuarios.objects.all()
    
    data={
        'usuarios':usuarios
    }
    
    return render(request, 'todos_usuarios.html', data)

def cargar_editar_usuario(request, id_usuario):
    usuario= get_object_or_404(Usuarios,id=id_usuario)
    form = UsuarioForm(instance=usuario)
    
    return render(request, 'editar_usuario.html', {'form': form, 'usuario': usuario})

def editar_usuario(request, id_usuario):
    usuario= get_object_or_404(Usuarios,id=id_usuario)
    
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('todos_usuarios')
    
    return render(request, 'editar_usuario.html', {'form': form, 'usuario': usuario})

def eliminar_usuario(request, id_usuario):
    usuario = get_object_or_404(Usuarios, id=id_usuario)
    
    if request.method == 'POST':
        usuario.delete()
        return redirect('todos_usuarios')
    
    return render(request, 'templates_rrhh/eliminar_usuario.html', {'usuario': usuario})