from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin,Group, Permission



class CustomUserManager(BaseUserManager):    
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El email es incorrecto')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    def  create_superuser(self, email, password=None ,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        
        return self.create_user(email,password, **extra_fields)
        

class Usuario(AbstractBaseUser, PermissionsMixin):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(null=True, blank=True)
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups',  # Nombre único
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',  # Nombre único
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
    
    TIPOS_USUARIO = [
        ('arrendatario', 'Arrendatario'),
        ('arrendador', 'Arrendador')
    ]
    foto_usuario = models.ImageField(upload_to='usuario/', null=True, blank=True)
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
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
   
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
   
    def __str__(self):
        return self.email

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
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='inmuebles', default=1)
    nombre = models.CharField(max_length=200)
    foto_inmueble = models.ImageField(upload_to='inmuebles/', null=True, blank=True)
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