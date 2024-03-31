from django.shortcuts import render
from .models import Participaciones
from juegos.models import Juego


def jugadores_principal(request):
    juegos = Juego.objects.all()
    mejores_por_juego = {}
    for juego in juegos:
        # Aquí asumimos que hay algún campo `puntaje` o similar para determinar el "mejor"
        # Ajuste este query según su modelo y lógica de negocio
        mejores = Participaciones.objects.filter(juego=juego)
        mejores_por_juego[juego.nombre] = mejores
        print(mejores)
    context = {'mejores_por_juego': mejores_por_juego}
    return render(request, 'jugadores/jugadores_principal.html', context)


def jugadores_registro(request):
    return render(request, 'jugadores/jugadores_registro.html')

