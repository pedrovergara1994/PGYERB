import base64
from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render
from django import forms
from django.shortcuts import redirect
import json

import hashlib

from data.models import Cliente
from data.models import Instrumento
from data.models import Carrito



def agregar_al_carrito(request, registro_id):    
    instru_encontrado = Instrumento.objects.filter(id=registro_id)
    lista_encontrado = list(instru_encontrado.values())
    print('lista_encontrado: ', lista_encontrado[0])
    id_instrumento_nuevo = lista_encontrado[0].get('id')
    email = request.session.get('cli-email')
    print('mi email is ', email)
    cliente = Cliente.objects.filter(mail=email)
    cliente_encontrado = list(cliente.values())
    print('cliente encontrado: ', cliente_encontrado[0])
    carrito = request.session.get(email)
    if carrito:
        print('carrito  ')
        detalle_instrumentos = carrito.get('detalle_instrumentos')
        #print('detalle_instrumentos : ', detalle_instrumentos)
        nuevo_total = 0
        detalle = {}
        existe = False
        nuevo_total += lista_encontrado[0].get('precio')
        for i in detalle_instrumentos:
            nuevo_total += i.get('monto')
            if i.get('id') == id_instrumento_nuevo:
                i['cantidad'] = i.get('cantidad') + 1
                i['monto'] = i.get('monto') + lista_encontrado[0].get('precio')
                existe = True
        
        if existe == False:
            detalle = {
                "id": lista_encontrado[0].get('id'), 
                "nombre": lista_encontrado[0].get('name'),
                "cantidad":1,
                "monto": lista_encontrado[0].get('precio'),
                "imagen": lista_encontrado[0].get('img')
            }
            detalle_instrumentos.append(detalle)    
               
               
                    
           
        
        
        carrito['detalle_instrumentos'] = detalle_instrumentos   
        carrito['total'] = nuevo_total   
        request.session[email] = carrito
        print('nuevo carrito: ', carrito)
    else:
        print('carrrio vacio ', carrito)
        carrito = {
            "usuario": email,
            "detalle_instrumentos": [
                {
                    "id": lista_encontrado[0].get('id'),
                    "nombre": lista_encontrado[0].get('name'),    
                    "cantidad":1,
                    "monto": lista_encontrado[0].get('precio'),
                    "imagen": lista_encontrado[0].get('img')
                }
            ],
            "total": lista_encontrado[0].get('precio')
        }
        print('nuevo carrito ', carrito.get('total'))
        request.session[email] = carrito
        request.session.get('')

# del request.session['']
    
    return redirect('catalogo')





def ir_carrito(request):
    email = request.session.get('cli-email')
    micarrito = request.session.get(email)
    if micarrito:
        detalle_instrumentos = micarrito.get('detalle_instrumentos')
        print('detalle_instrumentos: ', detalle_instrumentos)
        return render(request, 'appweb/productos/carrito.html', {"micarrito": detalle_instrumentos, "total": micarrito.get('total')})
    return render(request, 'appweb/productos/carrito.html', {})