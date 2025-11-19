from django.shortcuts import render, redirect,get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
import json
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')  
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user) 
            return redirect('home')  
        else:
            messages.error(request, "Usuario o contraseña incorrectos")

    return render(request, 'registration/login.html')

@login_required
def home_view(request):
    return render(request, 'core/home.html')

#productos

@login_required
def productos_view(request):
    return render(request, 'core/productos.html')

@login_required
def registrar_producto(request):

    if request.method == "POST":

        id_producto = request.POST.get('id')
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        vida_util = request.POST.get('vida')

        # Validación
        try:
            vida_num = int(vida_util)
            if vida_num <= 0:
                messages.error(request, "La vida útil debe ser mayor a 0.")
                return redirect('registrarProducto')
        except:
            messages.error(request, "La vida útil debe ser un número válido.")
            return redirect('registrarProducto')

        # Validación
        if Producto.objects.filter(id_producto=id_producto).exists():
            messages.error(request, "El código del producto ya existe.")
            return redirect('registrarProducto')
        
        producto = Producto(
            id_producto=id_producto,
            nombre=nombre,
            descripcion=descripcion,
            vida_util=vida_util
        )
        producto.save()

        messages.success(request, "Producto registrado correctamente.")
        return redirect('registrarProducto')  

    return render(request, "productos/reg_producto.html")



@login_required
def modificar_producto(request):
    productos = Producto.objects.all().order_by('id_producto')
    return render(request, 'productos/mod_producto.html', {'productos': productos})

@login_required
def editar_producto(request, id_producto):
    producto = get_object_or_404(Producto, id_producto=id_producto)

    if request.method == "POST":
        producto.nombre = request.POST.get("nombre")
        producto.descripcion = request.POST.get("descripcion")
        producto.vida_util = request.POST.get("vida")
        producto.save()

        messages.success(request, "Producto actualizado correctamente.")
        return render(request, 'productos/editar_producto.html', {"producto": producto})

    return render(request, 'productos/editar_producto.html', {"producto": producto})

@login_required
def eliminar_producto(request, id_producto):
    producto = get_object_or_404(Producto, id_producto=id_producto)
    productos = Producto.objects.all().order_by('id_producto')
    producto.delete()
    messages.success(request, "Producto eliminado correctamente.")
    return render(request, 'productos/mod_producto.html', {'productos': productos})

#recepcion

@login_required
def lista_recepciones(request):
    recepciones = Recepcion.objects.all().order_by('-fecha_recepcion')

    context = {
        'recepciones': recepciones
    }
    return render(request, 'recepcion/lista_recepcion.html', context)

@login_required
def agregar_recepcion(request):

    if request.method == 'POST':
        idr = request.POST.get('id_recepcion')
        prov = request.POST.get('nombre_proveedor')
        fecha = request.POST.get('fecha_recepcion')
        obs = request.POST.get('observaciones')

        Recepcion.objects.create(
            id_recepcion=idr,
            nombre_proveedor=prov,
            fecha_recepcion=fecha,
            observaciones=obs
        )
        recepcion = get_object_or_404(Recepcion, id_recepcion=idr)
        messages.success(request, "Recepción registrada correctamente.")
        return redirect('agregarDetalleRecepcion', id_recepcion=recepcion.id_recepcion)

    return render(request, 'recepcion/reg_recepcion.html')

@login_required
def agregar_detalle(request, id_recepcion):

    # 1. obtener la recepción asociada
    recepcion = get_object_or_404(Recepcion, id_recepcion=id_recepcion)

    # 2. obtener lista de productos
    productos = Producto.objects.all()

    # 3. si viene POST, guardar detalle
    if request.method == "POST":
        idproducto = request.POST.get("producto")
        cantidad = request.POST.get("cantidad")
        unidad = request.POST.get('unidad')
        lote = request.POST.get("lote")
        ubicacion = request.POST.get("ubicacion")

        # validación mínima
        if not idproducto or not cantidad:
            messages.error(request, "Debe completar todos los campos obligatorios.")
            return redirect("agregarDetalleRecepcion", id_recepcion=id_recepcion)

        producto_obj = get_object_or_404(Producto, id_producto=idproducto)

        # generar ID detalle automáticamente (tú puedes cambiar este formato)
        nuevo_id = f"DET-{Det_Recepcion.objects.count()+1}"

        # crear el detalle
        Det_Recepcion.objects.create(
            id_detalle=nuevo_id,
            idproducto=producto_obj,
            cantidad=cantidad,
            unidad=unidad,
            lote=lote,
            ubicacion=ubicacion,
            idrecepcion=recepcion
        )

        messages.success(request, "Detalle agregado correctamente.")

        # redirige al editor de recepción para ver todos los detalles
        return redirect("agregarDetalleRecepcion", id_recepcion=id_recepcion)

    # 4. retornar formulario vacío
    return render(request, "recepcion/detalle_recepcion.html", {
        "recepcion": recepcion,
        "productos": productos
    })

@login_required
def desglose_recepcion(request, id_recepcion):

    # Obtener la recepción
    recepcion = get_object_or_404(Recepcion, id_recepcion=id_recepcion)

    # Obtener todos los detalles ligados a la recepción
    detalles = Det_Recepcion.objects.filter(idrecepcion=recepcion)

    context = {
        'recepcion': recepcion,
        'detalles': detalles
    }

    return render(request, 'recepcion/desglose_recepcion.html', context)

@login_required
def editar_recepcion(request, id):
    recepcion = get_object_or_404(Recepcion, pk=id)
    detalles = Det_Recepcion.objects.filter(idrecepcion=recepcion)

    if request.method == 'POST':
        recepcion.nombre_proveedor = request.POST.get('nombre_proveedor')
        recepcion.fecha_recepcion = request.POST.get('fecha_recepcion')
        recepcion.observaciones = request.POST.get('observaciones')
        recepcion.save()

        messages.success(request, "Recepción actualizada correctamente.")
        return redirect('editar_recepcion', id=id)

    return render(request, 'recepcion/editar_recepcion.html', {
        'recepcion': recepcion,
        'detalles': detalles
    })

@login_required
def eliminar_recepcion(request, id_recepcion):

    recepcion = get_object_or_404(Recepcion, id_recepcion=id_recepcion)

    if request.method == "POST":
        recepcion.delete()
        messages.success(request, "Recepción y todos sus detalles fueron eliminados.")
        return redirect('recepciones')

    return render(request, 'recepcion/eliminar_recepcion.html', {
        'recepcion': recepcion
    })


@login_required
def editar_detalle(request, id_detalle):
    detalle = get_object_or_404(Det_Recepcion, id_detalle=id_detalle)
    productos = Producto.objects.all()

    if request.method == "POST":
        detalle.cantidad = request.POST.get("cantidad")
        detalle.unidad = request.POST.get("unidad") 
        detalle.idproducto_id = request.POST.get("idproducto")
        detalle.lote = request.POST.get("lote")
        detalle.ubicacion = request.POST.get("ubicacion")

        detalle.save()

        return redirect("recepcion/editar_detalle.html", id_recepcion=detalle.idrecepcion.id_recepcion)

    return render(request, "recepcion/editar_detalle.html", {
        "detalle": detalle,
        "productos": productos
    })

@login_required
def eliminar_detalle(request, id_detalle):

    detalle = get_object_or_404(Det_Recepcion, id_detalle=id_detalle)
    recepcion_id = detalle.idrecepcion.id_recepcion   # para volver atrás

    if request.method == "POST":
        detalle.delete()
        messages.success(request, "Detalle eliminado correctamente.")
        return redirect('desglose_recepcion', recepcion_id)

    return render(request, 'recepcion/eliminar_detalle.html', {
        'detalle': detalle
    })

def recepcion_view(request):
    return render(request, 'core/recepcion.html')

def confirmacion_view(request):
    return render(request, 'core/confirmacion.html')
