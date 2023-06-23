from django.urls import path
from . import views
from . import sessionview
from . import micuenta
from . import instrumentos

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('register_save', sessionview.register_save, name='register_save'),
    path('login_init', sessionview.login_init, name='login_init'),
    path('micuenta', micuenta.micuenta, name='micuenta'),
    path('crearimg', instrumentos.crear, name='crearimg'),
    path('catalogo', instrumentos.catalogo, name='catalogo'),
    path('crearinstrumento', instrumentos.crearinstrumento, name='crearinstrumento'),
    path('instrumento_save', instrumentos.instrumento_save, name='instrumento_save'),
]
