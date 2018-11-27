from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout

from Usuarios.models import Usuarios


def inicio_sesion(request):
    if request.POST:
        username = request.POST.get('usuario')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            usuario = Usuarios.objects.get(User=user)
            context = {
                'usuario_rut': usuario.rut,
                'es_docente': usuario.es_docente(),

            }
            return HttpResponseRedirect(reverse('usuarios:home', kwargs=context))

    logout(request)
    return render(request, 'templates/login.html', {})
