from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render
import hashlib

from data.models import Cliente


def micuenta(request):
    return render(request, 'appweb/micuenta/micuenta.html', {})
