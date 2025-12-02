from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from forneria import views
from forneriaRrhhApi import views as vistasApi
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
    path('', views.home, name='home'),
    path('ventas/', include('ventas.urls')),
    path('rrhh/', include('rrhh.urls')),
    path('api/', include('forneriaRrhhApi.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
