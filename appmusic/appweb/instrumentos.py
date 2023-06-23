import base64
from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render
from django import forms
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

