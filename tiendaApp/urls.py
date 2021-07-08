from django.urls import path
from .views import index,base,about,contacto,acceder,salir,registrar,carrito, infoproducto


app_name = "Tienda"
urlpatterns = [
    path('', index, name = 'Index'), #Vista del Home
    path('base', base, name = 'Base'), #Vista de la Base
    path('carrito', carrito, name = 'Carrito'), #Vista del carrito
    path('infoproducto', infoproducto, name = 'Infoproducto'), #Vista informacion del producto
    path('about', about, name = 'About'), #Vista de About
    path('contacto', contacto, name = 'Contacto'), #Vista de Contacto
    path('acceder', acceder, name = 'Acceder'), #Vista de Login
    path('salir', salir, name = 'Salir'), #Vista de Logout
    path('registrar', registrar, name = 'Registrar'), #Vista de Logout
]
