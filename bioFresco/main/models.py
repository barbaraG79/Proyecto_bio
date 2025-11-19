from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):  
    cargo = models.CharField(max_length=30, blank=True, null=True)
    tipo = models.CharField(
        max_length=1,
        choices=[('A', 'Administrador'), ('R', 'Repartidor')],
        default='R'
    )

    def __str__(self):
        return self.username

class Producto(models.Model):
    id_producto = models.CharField(max_length=30, primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100, null=True, blank=True)
    vida_util = models.CharField(max_length=10)
    

class Recepcion (models.Model):
    id_recepcion = models.CharField(max_length=30, primary_key=True)
    nombre_proveedor = models.CharField(max_length=100)
    fecha_recepcion= models.DateField(null=True, blank =True)
    observaciones = models.CharField(max_length=100, null=True, blank=True)

class Det_Recepcion(models.Model):
    id_detalle = models.CharField(max_length=30, primary_key=True)
    cantidad = models.CharField(max_length=10)
    unidad = models.CharField (max_length=10, null=True)
    
    # foreign keys
    idproducto = models.ForeignKey(
        Producto,
        on_delete=models.CASCADE,      
        related_name='detalles_recepcion'
    )
    idrecepcion = models.ForeignKey(
        Recepcion,
        on_delete=models.CASCADE,      
        related_name='detalles'
    )
    lote = models.CharField(max_length=30, null=True)
    ubicacion =  models.CharField(max_length=60, blank=True)
