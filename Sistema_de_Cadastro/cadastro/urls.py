from django.contrib import admin
from django.urls import path
from cad import views

# view define o que vao acontecer quando o chagar no link
urlpatterns = [
    # rota, view responsavel, nome de referencia
    #ex = views
    path('',views.home, name = 'home'),
    path('usuarios/', views.usuarios, name = "listagem_usuarios") # o name é o mesmo espcificado lá no html
]
