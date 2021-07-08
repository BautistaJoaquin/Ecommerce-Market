from .models import Categoria
from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth.models import User

# Create your views here.

def alta(request):
    if request.method=="POST":
       form=FormProducto(request.POST, request.FILES)
       if form.is_valid():
           form.save()
           
           redirect('Tienda:Index')
    else:
        form=FormProducto()
    return render(request, "producto/altaProducto.html",{
        "form": form,})

def modificar(request):
    return render(request,'producto/modificarProducto.html')
