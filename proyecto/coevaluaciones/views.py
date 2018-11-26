from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.shortcuts import render

from coevaluaciones.models import Usuario


# Create your views here.
def index(request):
    return render(request, '../Templates/login.html', {})


def inicio_sesion(request):
    if request.POST:
        username = request.POST.get('inputUser')
        password = request.POST.get('inputPassword')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)

        usuario = Usuario.objects.get(User=user)

        return HttpResponseRedirect(reverse('usuarios:perfil', kwargs={'usuario_id': usuario.id}))

    logout(request)

    return render(request, '/Templates/home-vista-alumno.html', {})

