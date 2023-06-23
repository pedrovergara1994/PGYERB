from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render
import hashlib

from data.models import Cliente


def login_init(request):

    email = request.POST.get('username')
    password = request.POST.get('password')
    print(email)
    print(password)
    clave = password.encode('utf-8')
    pwd = hashlib.new("sha256", clave)
    print(pwd.hexdigest())
    find_cliente = Cliente.objects.filter(mail=email, password=pwd.hexdigest())
    print(find_cliente)
    if find_cliente:
        return render(request, 'appweb/index.html', {"cliente": find_cliente})
    else:
        return render(request, 'appweb/session/login.html', {})


def register_save(request):
    print(request.POST['firstname'])
    firstname = request.POST.get('firstname')
    lastname = request.POST.get('lastname')
    rut = request.POST.get('rut')
    phono = request.POST.get('phone')
    email = request.POST.get('email')
    password = request.POST.get('psw')
    password2 = request.POST.get('psw-repeat')
    if password != password2:
        message = 'Las contraseñas no coinciden'
        return render(request, 'appweb/session/register.html', {"message_error", message})

    clave = password.encode('utf-8')

    pwd = hashlib.new("sha256", clave)
    cliente = Cliente(
        first_name=firstname,
        last_name=lastname,
        rut=rut,
        phone=phono,
        mail=email,
        password=pwd.hexdigest(),
    )
    print('Buscar cliente con rut : ', rut)
    find_cliente = Cliente.objects.filter(rut__icontains=rut)
    print('cliente encontrado: ', str(find_cliente))
    if find_cliente:
        print('Cliente ya existe')
        return render(request, 'appweb/session/register.html', {})
    else:
        cliente.save()
    return render(request, 'appweb/session/login.html', {})
