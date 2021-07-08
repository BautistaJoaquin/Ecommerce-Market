from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib import auth, messages
from .forms import SignUpForm
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from productoapp.models import Producto

# Create your views here.
def base(request):
    return render(request,'tienda/base.html')

def index(request):
    productos_tresultimos = Producto.objects.order_by('-id')[:3]
    productos_antesieteultimos = Producto.objects.order_by('-id')[3:10]
    
    return render(request,'tienda/index.html',{'tresultimos':productos_tresultimos, 'sieteultimos':productos_antesieteultimos},)

def carrito(request):
    productos = Producto.objects.all().order_by()
    return render(request,'tienda/carrito.html',{'form':productos},)

def infoproducto(request):
    productos = Producto.objects.all().order_by()
          
    return render(request,'tienda/infoproducto.html',{'form':productos},)

def about(request):
    return render(request,'tienda/about.html')

def contacto(request):
    return render(request,'tienda/contacto.html')

def acceder(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
       
        if user is not None:
           
            login(request, user)
            return redirect("Tienda:Index")
        
        else:
            messages.error(request, 'Datos incorrectos username/password')
    return render(request,'tienda/login.html')

def salir(request):
    logout(request)
    messages.success(request,F"Tu sesión se ha cerrado correctamente")
    return redirect("Tienda:Index")

def registrar(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            print(username)
            print(raw_password)
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('Tienda:Index')
    else:
        form = SignUpForm()
    return render(request,'tienda/registrar.html', {'form': form})


