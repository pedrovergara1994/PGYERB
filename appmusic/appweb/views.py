from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render


def init():
    doc_externo = open("D:\Desarrollos\django\app-web\appmusic\appmusic\view\index.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()
    document = plt.render(ctx)
    return HttpResponse(document)


def index(request):
    return render(request, 'appweb/index.html', {})


def nosotros(request):
    return render(request, 'appweb/nosotros.html', {})


def login(request):
    return render(request, 'appweb/session/login.html', {})


def register(request):
    return render(request, 'appweb/session/register.html', {})
