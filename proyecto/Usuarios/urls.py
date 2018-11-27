from django.urls import path

from Usuarios.views import inicio_sesion
from Usuarios.views import perfil_usuario
from Usuarios.views import registrar_usuario
from Usuarios.views import cerrar_sesion

urlpatterns = [
  path('', inicio_sesion, name='inicio'),
  path('registro', registrar_usuario, name='registro'),
  path('home/<int:usuario_rut>/', perfil_usuario, name='home'),
  path('logout/', cerrar_sesion, name='logout')
]
