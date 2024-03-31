from django.urls import path
from .views import (jugadores_registro,
                    jugadores_principal
                    )

urlpatterns = [
    path('jugadores/', jugadores_principal, name="jugadores_principal"),
    path('jugadores/registro', jugadores_registro, name="jugadores_registro"),
]
