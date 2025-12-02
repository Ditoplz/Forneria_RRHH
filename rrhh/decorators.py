from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required

def grupo_requerido(*nombres_grupo):
    def decorator(view_func):
        @login_required
        def _wrapped_view(request, *args, **kwargs):
            if request.user.groups.filter(name__in=nombres_grupo).exists():
                return view_func(request, *args, **kwargs)
            return HttpResponseForbidden("No tienes permisos para acceder a esta vista")
        return _wrapped_view
    return decorator