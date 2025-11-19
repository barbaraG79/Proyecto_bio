from django.urls import path
from .views import *

urlpatterns = [
    path('',login_view,name = 'login'),
    path('home', home_view, name='home'),
    path('productos',productos_view, name='productos'),
    path('registrar_producto', registrar_producto, name='registrarProducto'),
    path('modificar_producto',modificar_producto, name='modificarProducto'),
    path('productos/editar/<str:id_producto>/', editar_producto, name='editar_producto'),
    path('productos/eliminar/<str:id_producto>/', eliminar_producto, name='eliminar_producto'),
    path('confirmacion', confirmacion_view, name='confirmacion'),
    # RECEPCION
    path('recepcion',recepcion_view,name='recepcion'),
    path('recepcion/agregar/', agregar_recepcion, name='agregar_recepcion'),
    path('recepcion/<str:id>/editar/', editar_recepcion, name='editar_recepcion'),
    path('recepcion/<str:id_recepcion>/eliminar/', eliminar_recepcion, name='eliminar_recepcion'),
    path('recepcion/listado/', lista_recepciones, name='recepciones'),
    path('recepciones/<str:id_recepcion>/', desglose_recepcion, name='desglose_recepcion'),
    # DETALLES 
    path('recepcion/<str:id_recepcion>/detalle',agregar_detalle, name='agregarDetalleRecepcion' ),
    path('detalle/<str:id_detalle>/editar/', editar_detalle, name='editar_detalle'),
    path('detalle/<str:id_detalle>/eliminar/', eliminar_detalle, name='eliminar_detalle'),

    # DETALLES RECEPCION
    # path('detalle/agregar/<str:id_recepcion>/', views.agregar_detalle, name='agregar_detalle'),
    # path('detalle/<str:id_detalle>/editar/', editar_detalle, name='editar_detalle'),
    # path('detalle/<str:id_detalle>/eliminar/', views.eliminar_detalle, name='eliminar_detalle'),
    # path('logout',exit,name='exit')
]