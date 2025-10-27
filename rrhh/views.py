from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, 'rrhh/index.html')

@login_required
def gestor_rrhh(request):
    return render(request, 'gestor_rrhh.html')