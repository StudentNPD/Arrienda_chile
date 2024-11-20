from django.db import models
from django.utils import timezone

class Inmueble(models.Model):
    TIPOS_INMUEBLE = [
        ('casa', 'Casa'),
        ('departamento', 'Departamento'),
        ('parcela', 'Parcela')
    ]

    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    m2_construidos = models.FloatField()
    m2_totales = models.FloatField()
    estacionamientos = models.IntegerField()
    habitaciones = models.IntegerField()
    banos = models.IntegerField()
    direccion = models.CharField(max_length=200)
    comuna = models.CharField(max_length=100)
    tipo_inmueble = models.CharField(
        max_length=50, 
        choices=TIPOS_INMUEBLE
    )
    precio_mensual = models.IntegerField()
   
    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    TIPOS_USUARIO = [
        ('arrendatario', 'Arrendatario'),
        ('arrendador', 'Arrendador')
    ]

    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    rut = models.CharField(max_length=12, unique=True)
    direccion = models.TextField()
    telefono = models.CharField(max_length=15)
    email = models.CharField(max_length=100, unique=True)
    tipo_usuario = models.CharField(
        max_length=20, 
        choices=TIPOS_USUARIO
    )
   
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