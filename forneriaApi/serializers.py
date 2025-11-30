from rest_framework import serializers
from rrhh.models import Empleado,Contrato,Liquidacion,AuthUser,Cargo,Direccion

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'

class ContratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contrato
        fields = '__all__'

class LiquidacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Liquidacion
        fields = '__all__'

class AuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = '__all__'

class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = '__all__'