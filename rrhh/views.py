from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

from rrhh.models import Empleado, Cargo
from .forms import EmpleadoForm, CargoForm

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

@login_required
def crear_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
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
    else:
        form = EmpleadoForm(instance=empleado)
    
    return render(request, 'mantenedor_empleados.html', {'form': form, 'empleado': empleado})

def eliminar_empleado(request, id_empleado):
    empleado = get_object_or_404(Empleado, id=id_empleado)
    
    if request.method == 'POST':
        empleado.delete()
        
    return render(request, 'mantenedor_empleados.html')


@login_required
def crear_cargo(request):
    if request.method == 'POST':
        form = CargoForm(request.POST)
        if form.is_valid():
            form.save()
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
    else:
        form = CargoForm(instance=cargo)
    
    return render(request, 'mantenedor_cargos.html', {'form': form, 'cargo': cargo})

def eliminar_cargo(request, id_cargo):
    cargo = get_object_or_404(Cargo, id=id_cargo)
    
    if request.method == 'POST':
        cargo.delete()
        
    return render(request, 'mantenedor_cargos.html')