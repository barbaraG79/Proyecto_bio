from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
import json
from .models import *
from django.contrib.auth.hashers import check_password
from .forms import ProductoForm
# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            usuario = Usuario.objects.get(id_usuario=username)
            if check_password(password, usuario.password):
                # Guarda los datos:
                request.session['username'] = usuario.id_usuario
                return redirect('/home') #redirecciona al home
            else:
                messages.error(request, 'Contraseña incorrecta')
        except Usuario.DoesNotExist:
            messages.error(request, 'Usuario incorrecto')

    return render(request, 'registration/login.html')

def home_view(request):
    username = request.session.get('username')
    if not username:
        return redirect('login')
    
    usuario = Usuario.objects.get(id_usuario=username)
    return render(request, 'core/home.html', {'usuario': usuario})

def productos_view(request):
    return render(request, 'core/productos.html')

def registrar_producto(request):
    if request.method != 'POST':
        return JsonResponse({'success': False, 'message': 'Método no permitido'}, status=405)

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'success': False, 'message': 'JSON inválido'}, status=400)

    id_producto = data.get('id_producto')
    nombre = data.get('nombre')
    descripcion = data.get('descripcion', '')
    vida_util = data.get('vida_util')

    if not id_producto or not nombre or not vida_util:
        return JsonResponse({'success': False, 'message': 'Faltan campos requeridos'}, status=400)

    if Producto.objects.filter(id_producto=id_producto).exists():
        return JsonResponse({'success': False, 'message': 'El producto ya existe'})

    Producto.objects.create(
        id_producto=id_producto,
        nombre=nombre,
        descripcion=descripcion,
        vida_util=vida_util
    )

    return JsonResponse({'success': True, 'message': 'Producto registrado correctamente'})

def registrarProducto_view(request):
    return render(request, 'core/reg_producto.html')

def modificarProducto_view(request):
    return render(request, 'core/mod_producto.html')

def recepcion_view(request):
    return render(request, 'core/recepcion.html')

def recepcionProducto_view(request):
    return render(request, 'core/recepcion_producto.html')

def confirmacion_view(request):
    return render(request, 'core/confirmacion.html')
