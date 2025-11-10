from django.contrib import admin
from django.contrib.auth.hashers import make_password
from .models import Usuario
# Register your models here.


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id_usuario', 'nombre', 'cargo', 'email', 'tipo')
    # Opcional: campos que se pueden buscar
    search_fields = ('id_usuario', 'nombre', 'email')

    def save_model(self, request, obj, form, change):
        """
        Este método se ejecuta al guardar un usuario desde admin.
        Si la contraseña fue cambiada, la hashea antes de guardar.
        """
        # Solo hasheamos si es un objeto nuevo o si la contraseña se cambió manualmente
        if 'password' in form.changed_data:
            obj.password = make_password(obj.password)
        super().save_model(request, obj, form, change)

admin.site.register(Usuario, UsuarioAdmin)