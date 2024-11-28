from django.db import models
from django.utils import timezone


class Region(models.Model):
    codigo = models.CharField(max_length=2, primary_key=True)
    nombre = models.CharField(max_length=100, unique=True )

    def __str__(self):
        return self.nombre


class Comuna(models.Model):
    nombre = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name="comuna")

    def __str__(self):
        return self.nombre
    
class Inmueble(models.Model):
    TIPOS_INMUEBLE = [
        ('casa', 'Casa'),
        ('departamento', 'Departamento'),
        ('parcela', 'Parcela')
    ]

    nombre = models.CharField(max_length=200)
    foto_inmueble = models.ImageField(upload_to='./static/img/inmuebles/', null=True, blank=True)
    descripcion = models.TextField()
    m2_construidos = models.FloatField()
    m2_totales = models.FloatField()
    estacionamientos = models.IntegerField()
    habitaciones = models.IntegerField()
    banos = models.IntegerField()
    direccion = models.CharField(max_length=200)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True, blank=True)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    tipo_inmueble = models.CharField( max_length=50, choices=TIPOS_INMUEBLE)
    precio = models.IntegerField(null=True, blank=True)
    
    def precio_clp(self):
        return f"${self.precio:,}".replace(",", ".")

   
    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    TIPOS_USUARIO = [
        ('arrendatario', 'Arrendatario'),
        ('arrendador', 'Arrendador')
    ]
    foto_usuario = models.ImageField(upload_to='./static/img/usuario/', null=True, blank=True)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    rut = models.CharField(max_length=12, unique=True)
    direccion = models.TextField()
    telefono = models.CharField(max_length=15, unique=True)
    email = models.CharField(max_length=100, unique=True)
    tipo_usuario = models.CharField(
        max_length=20, 
        choices=TIPOS_USUARIO
    )
    #clave = models.CharField(max_length=20)
   
    def __str__(self):
        return self.nombre

class RegistroArriendo(models.Model):
    ESTADOS_ARRIENDO = [
        ('pendiente', 'Pendiente'),
        ('en_proceso', 'En Proceso'),
        ('aceptado', 'Aceptado'),
        ('cancelado', 'Cancelado'),
        ('finalizado', 'Finalizado')
    ]

    usuario_arrendador = models.ForeignKey(
        Usuario, 
        on_delete=models.CASCADE, 
        related_name='arriendos_ofrecidos'
    )
    usuario_arrendatario = models.ForeignKey(
        Usuario, 
        on_delete=models.CASCADE, 
        related_name='arriendos_solicitados'
    )
    inmueble = models.ForeignKey(
        Inmueble, 
        on_delete=models.CASCADE
    )
    estado = models.CharField(
        max_length=20, 
        choices=ESTADOS_ARRIENDO, 
        default='pendiente'
    )
    fecha_inicio = models.DateField(
        null=True, 
        blank=True
    )
    fecha_fin = models.DateField(
        null=True, 
        blank=True
    )
    fecha_solicitud = models.DateTimeField(
        default=timezone.now
    )
    
    def __str__(self):
        return self.inmueble.nombre

class UsuarioInmuebles(models.Model):
    inmueble = models.ForeignKey(
        Inmueble, 
        on_delete=models.CASCADE
    )
    usuario_arrendador = models.ForeignKey(
        Usuario, 
        on_delete=models.CASCADE
    )
    
    class Meta:
        unique_together = ('inmueble', 'usuario_arrendador')
    
    def __str__(self):
        return self.usuario_arrendador.nombre