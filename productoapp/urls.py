from django.urls import path
from .views import alta,modificar

app_name = "PRODUCTO"

urlpatterns = [
    
    path('alta', alta, name = 'Alta'), #Vista de Alta de producto
    path('modificar', modificar, name = 'Modificar'), #Vista de Modificar producto
    
]
