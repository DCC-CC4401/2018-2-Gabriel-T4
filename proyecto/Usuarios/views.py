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
                'usuario': usuario,
                'es_alumno': not usuario.es_docente(),
                'es_docente': usuario.es_docente(),

                # TODO Mandar las coevaluaciones en el context
                'ultimas_coevaluaciones': []

            }
            return HttpResponseRedirect(reverse('usuarios:home', kwargs=context))

    logout(request)
    return render(request, 'templates/login.html', {})


def home_usuario(request):
    if not request.user.is_authenticated:
        return render(request, 'templates/login.html'
                      )
    usuario = Usuarios.objects.get(User=request.user)
    context = {
        'usuario': usuario,
        'es_alumno': not usuario.es_docente(),
        'es_docente': usuario.es_docente(),

        # TODO Mandar las coevaluaciones en el context
        'ultimas_coevaluaciones': []
    }

    return render(request, 'templates/Usuarios.html', context)
