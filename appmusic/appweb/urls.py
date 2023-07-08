from django.urls import path
from . import views
from . import sessionview
from . import micuenta
from . import instrumentos
from . import carrito

urlpatterns = [
    path('', views.index, name='index'),
    path('inicio', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('register_save', sessionview.register_save, name='register_save'),
    path('login_init', sessionview.login_init, name='login_init'),
    path('logout', sessionview.logout, name='logout'),
    path('micuenta', micuenta.micuenta, name='micuenta'),
    path('crearimg', instrumentos.crear, name='crearimg'),
    path('catalogo', instrumentos.catalogo, name='catalogo'),
    path('crearinstrumento', instrumentos.crearinstrumento, name='crearinstrumento'),
    path('instrumento_save', instrumentos.instrumento_save, name='instrumento_save'),
    path('catalogo/<int:registro_id>/', instrumentos.eliminar_instrumento, name='eliminar_instrumento'),
    path('catalogo<int:registro_id>/', carrito.agregar_al_carrito, name='carrito_agregar'),
    path('carrito', carrito.ir_carrito, name='carrito_micarrito'),
    path('carrito_eliminar/', instrumentos.eliminar_carrito, name='carrito_eliminar'),
    path('carrito_eliminar/inicio', views.index, name='index'),
    path('carrito_eliminar/login', views.login, name='login'),
    path('carrito_eliminar/register', views.register, name='register'),
    path('carrito_eliminar/nosotros', views.nosotros, name='nosotros'),
    path('carrito_eliminar/register_save', sessionview.register_save, name='register_save'),
    path('carrito_eliminar/login_init', sessionview.login_init, name='login_init'),
    path('carrito_eliminar/logout', sessionview.logout, name='logout'),
    path('carrito_eliminar/micuenta', micuenta.micuenta, name='micuenta'),
    path('carrito_eliminar/crearimg', instrumentos.crear, name='crearimg'),
    path('carrito_eliminar/catalogo', instrumentos.catalogo, name='catalogo'),
    path('carrito_eliminar/crearinstrumento', instrumentos.crearinstrumento, name='crearinstrumento'),
    path('carrito_eliminar/instrumento_save', instrumentos.instrumento_save, name='instrumento_save'),
    path('carrito_eliminar/catalogo/<int:registro_id>/', instrumentos.eliminar_instrumento, name='eliminar_instrumento'),
    path('carrito_eliminar/catalogo<int:registro_id>/', carrito.agregar_al_carrito, name='carrito_agregar'),
    path('carrito_eliminar/carrito', carrito.ir_carrito, name='carrito_micarrito'),
    path('carrito_eliminar/contacto', views.contacto, name='nosotros'),
    path('contacto', views.contacto, name='nosotros'),
]
