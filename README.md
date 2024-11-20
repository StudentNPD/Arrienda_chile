# Plataforma de Arriendos de Inmuebles

## Descripción del Proyecto
Plataforma web para gestión de arriendos de inmuebles, que permite a usuarios registrarse como arrendatarios o arrendadores, publicar, buscar y solicitar propiedades.

## Características Principales

### Usuarios
- Registro de usuarios
- Dos tipos de usuarios: Arrendatarios y Arrendadores
- Actualización de datos personales

### Arrendatarios
- Listar propiedades por comuna
- Generar solicitudes de arriendo
- Explorar detalles de inmuebles

### Arrendadores
- Publicar propiedades
- Gestionar propiedades (listar, editar, eliminar)
- Aceptar solicitudes de arrendamiento

## Tecnologías Utilizadas
- Framework: Django
- Base de Datos: PostgreSQL
- Lenguaje: Python

## Requisitos Previos
- Python 3.13.0
- PostgreSQL
- pip
- virtualenv

## Instalación

### 1. Clonar Repositorio
```bash
git clone https://github.com/tu-usuario/arriendos-proyecto.git
cd arriendos-proyecto
```

### 2. Configurar Entorno Virtual
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar Base de Datos
- Crear base de datos en PostgreSQL
- Configurar credenciales en `settings.py`

### 5. Migraciones
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Ejecutar Servidor
```bash
python manage.py runserver
```

## Estructura del Proyecto
```
arriendos_project/
│
├── propiedades/
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── usuarios/
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
└── arriendos_project/
    ├── settings.py
    └── urls.py
```

## Configuración de Modelos

### Usuario
```python
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
```

### Propiedad
```python
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
```

## Modelos Principales
- Usuario
- UsuarioInmuebles
- Inmueble
- RegistroArriendo

## Funcionalidades Pendientes
- [x] Modelo de datos
- [ ] Implementar autenticación
- [ ] Desarrollar vistas para gestión de inmuebles
- [ ] Crear formularios de registro de arriendo
