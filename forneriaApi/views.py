from django.shortcuts import render
from django.contrib.auth.models import User
from rrhh.models import Empleado,Contrato,Liquidacion,AuthUser,Cargo
from django.http import JsonResponse
from forneriaApi.serializers import EmpleadoSerializer,ContratoSerializer,LiquidacionSerializer,AuthUserSerializer,CargoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

def empleadosApi(request):
    empleados = Empleado.objects.all()
    data = {
        'empleados':list(
            empleados.values(
                'id',
                'nombres',
                'a_paterno',
                'a_materno',
                'run',
                'correo',
                'fono',
                'id_direccion',
                'user',
                'visible'
            )
        )
    }
    return JsonResponse(data)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def empleado_listado(request):
    if request.method == 'GET':
        empleados = Empleado.objects.all()
        serializer = EmpleadoSerializer(empleados, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = EmpleadoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def empleado_detalle(request, pk):
    try:
        empleado = Empleado.objects.get(pk=pk)
    except Empleado.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = EmpleadoSerializer(empleado)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = EmpleadoSerializer(empleado, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        empleado.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def liquidacionesApi(request):
    liquidaciones = Liquidacion.objects.all()
    data = {
        'liquidaciones':list(
            liquidaciones.values(
                'id',
                'empleado',
                'periodo',
                'bruto',
                'liquido',
                'visible'
                )
        )
    }
    return JsonResponse(data)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def liquidacion_listado(request):
    if request.method == 'GET':
        liquidaciones = Liquidacion.objects.all()
        serializer = LiquidacionSerializer(liquidaciones, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = LiquidacionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def liquidacion_detalle(request, pk):
    try:
        liquidacion = Liquidacion.objects.get(pk=pk)
    except Liquidacion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = LiquidacionSerializer(liquidacion)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = LiquidacionSerializer(liquidacion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        liquidacion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



def cargosApi(request):
    cargos = Cargo.objects.all()
    data = {
        'cargos':list(
            cargos.values(
                'id',
                'nombre',
                'descripcion',
                'visible'
            )
        )
    }
    return JsonResponse(data)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def cargo_listado(request):
    if request.method == 'GET':
        cargos = Cargo.objects.all()
        serializer = CargoSerializer(cargos, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = CargoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def cargo_detalle(request, pk):
    try:
        cargo = Cargo.objects.get(pk=pk)
    except Cargo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CargoSerializer(cargo)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = CargoSerializer(cargo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        cargo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def contratosApi(request):
    contratos = Contrato.objects.all()
    data = {
        'contratos':list(
            contratos.values(
                'id',
                'detalle_contrato',
                'fecha_inicio',
                'fecha_fin',
                'empleado',
                'cargo',
                'departamento',
                'visible'
            )
        )
    }
    return JsonResponse(data)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def contrato_listado(request):
    if request.method == 'GET':
        contratos = Contrato.objects.all()
        serializer = ContratoSerializer(contratos, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = ContratoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def contrato_detalle(request, pk):
    try:
        contrato = Contrato.objects.get(pk=pk)
    except Contrato.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ContratoSerializer(contrato)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = ContratoSerializer(contrato, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        contrato.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



def AuthUserApi(request):
    usuarios = AuthUser.objects.all()
    data = {
        'usuarios':list(
            usuarios.values(
                'id',
                'username',
                'password',
                'first_name',
                'last_name',
                'email',
                'is_staff',
                'is_active',
                'date_joined',
                'last_login',
                'visible'
            )
        )
    }
    return JsonResponse(data)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def usuario_listado(request):
    if request.method == 'GET':
        usuarios = AuthUser.objects.all()
        serializer = AuthUserSerializer(usuarios, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = AuthUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def usuario_detalle(request, pk):
    try:
        usuario = AuthUser.objects.get(pk=pk)
    except AuthUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = AuthUserSerializer(usuario)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = AuthUserSerializer(usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
