from django.contrib import admin
from .models import Inmueble, Usuario, RegistroArriendo, UsuarioInmuebles

# Register your models here.
admin.site.register(Inmueble)
admin.site.register(Usuario)
admin.site.register(RegistroArriendo)
admin.site.register(UsuarioInmuebles)