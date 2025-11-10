from django.urls import path
from .views import *

urlpatterns = [
    path('',login_view,name = 'login'),
    path('home', home_view, name='home'),
    path('productos',productos_view, name='productos'),
    path('registrar_producto',registrarProducto_view, name='registrarProducto'),
    path('registro_producto', registrar_producto, name='registro_producto'),
    path('modificar_producto',modificarProducto_view, name='modificarProducto'),
    path('recepcion',recepcion_view,name='recepcion'),
    path('agregar_producto',recepcionProducto_view, name='recepcionProducto'),
    path('confirmacion', confirmacion_view, name='confirmacion'),
    # path('logout',exit,name='exit')
]