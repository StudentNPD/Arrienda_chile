from django.contrib import admin
from .models import Inmueble, Usuario, RegistroArriendo, UsuarioInmuebles, Region, Comuna

# Register your models here.
class InmuebleAdmin(admin.ModelAdmin):
    # Columnas a mostrar en el panel 
    list_display = ("nombre","usuario", "foto_inmueble" ,"descripcion", "direccion", "comuna","region", "tipo_inmueble", "precio", "m2_construidos", "m2_totales", "estacionamientos", "habitaciones", "banos")
    # Busqueda especifica
    search_fields = ["nombre", "comuna","tipo_inmueble"]
    # Filtro
    list_filter = ["tipo_inmueble", "comuna"]

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("nombre","foto_usuario", "apellido","rut", "direccion","telefono","email","password","tipo_usuario")
    search_fields = ["rut","nombre","apellido"]
    list_filter = ["rut","nombre","apellido","direccion","tipo_usuario"]
    
class RegistroArriendoAdmin(admin.ModelAdmin):
    list_display = ("usuario_arrendador","usuario_arrendatario","inmueble","estado","fecha_inicio")
    search_fields = ["usuario_arrendador","inmueble","estado"]
    list_filter = ["usuario_arrendador","usuario_arrendatario","inmueble"]
class UsuarioInmueblesAdmin(admin.ModelAdmin):
    list_display = ("inmueble","usuario_arrendador")
    search_fields = ["inmueble","usuario_arrendador"]
    list_filter = ["inmueble","usuario_arrendador"]
class ComunaAdmin(admin.ModelAdmin):
    list_display = ("nombre","region")
    search_fields = ["nombre","region"]
    list_filter = ["nombre","region"]
class RegionAdmin(admin.ModelAdmin):
    list_display = ("nombre","codigo")
    search_fields = ["nombre","codigo"]
    list_filter = ["nombre","codigo"]


admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Inmueble, InmuebleAdmin)
admin.site.register(UsuarioInmuebles, UsuarioInmueblesAdmin)
admin.site.register(RegistroArriendo, RegistroArriendoAdmin)
admin.site.register(Comuna, ComunaAdmin)
admin.site.register(Region, RegionAdmin)
