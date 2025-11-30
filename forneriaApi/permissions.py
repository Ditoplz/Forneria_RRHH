from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)

class IsRRHH(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.groups.filter(name='RRHH').exists())

class IsEmpleado(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.groups.filter(name='Empleado').exists())