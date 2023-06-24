import base64
from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render
from django import forms
from django.shortcuts import redirect
import hashlib

from data.models import Cliente
from data.models import Instrumento


def crear(request):
    return render(request, 'appweb/micuenta/micuenta.html', {})




def crearinstrumento(request):
    return render(request, 'appweb/productos/crear.html', {})


def catalogo(request):
    instrumentos = Instrumento.objects.all()
    return render(request, 'appweb/productos/catalogo.html', {"instrumentos": instrumentos})

def eliminar_carrito(request):
    print('Carrito eliminado')
    email = request.session.get('cli-email')
    del request.session[email]
    return catalogo(request)

def instrumento_save(request):
    try:
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        precio = request.POST.get('precio')
        print(request.POST)
        img = request.FILES 
        print(img)
        print(img.get('imagen'))
        img_binary = base64.b64encode(img.get('imagen').read()).decode('utf-8')
        print(img_binary)
        instrumento = Instrumento(
            name=name,
            desc=desc,
            precio=precio,
            img=img_binary
        )
        instrumento.save() 
        return catalogo(request)
    except Exception as e:
        print(e)
        return crearinstrumento(request)   

def eliminar_instrumento(request, registro_id):
    instrumento = Instrumento.objects.filter(id=registro_id)
    instrumento.delete()
    print('Registro ', registro_id, ' eliminado')
    return redirect('catalogo')