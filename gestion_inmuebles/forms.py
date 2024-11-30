from django import forms 
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Usuario, Inmueble
from django.contrib.auth.forms import UserCreationForm



    
class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = [
            'nombre',
            'apellido',
            'foto_usuario',
            'rut',
            'direccion',
            'telefono',
            'email',
            'tipo_usuario',
            'password1',
            'password2'
        ]
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'foto_usuario': 'Foto de Perfil',
            'rut': 'RUT',
            'direccion': 'Dirección',
            'telefono': 'Teléfono',
            'email': 'Correo Electrónico',
            'tipo_usuario': 'Tipo de Usuario'
        }
       
        widgets = {
            'tipo_usuario': forms.Select(choices=Usuario.TIPOS_USUARIO),
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre',
                }
            ),
            'apellido': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Apellido',
                }
            ),
            'rut': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'RUT',
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Dirección',
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Teléfono',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Correo Electrónico',
                }
            )
        }

    # Campos de contraseña
    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Contraseña'
            }
        )
    )
    password2 = forms.CharField(
        label='Confirmar Contraseña',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Confirmar Contraseña'
            }
        )
    )
        
class InmuebleForm(ModelForm):
    class Meta:
        model = Inmueble
        fields = [
            'nombre','usuario' ,'foto_inmueble', 'descripcion', 'm2_construidos', 'm2_totales', 
            'estacionamientos', 'habitaciones', 'banos', 'direccion', 'region', 
            'comuna', 'tipo_inmueble', 'precio'
        ]
        labels = {
            'nombre': '',
            'foto_inmueble': '',
            'descripcion': '',
            'm2_construidos': '',
            'm2_totales': '',
            'estacionamientos': '',
            'habitaciones': '',
            'banos': '',
            'direccion': '',
            'region': 'Region',
            'comuna': 'Comuna',
            'tipo_inmueble': 'Tipo de Inmueble',
            'precio': '',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el nombre del inmueble'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Descripción detallada del inmueble',
                'rows': 4
            }),
            'm2_construidos': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Metros cuadrados construidos'
            }),
            'm2_totales': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Metros cuadrados totales'
            }),
            'estacionamientos': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Cantidad de estacionamientos'
            }),
            'habitaciones': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Cantidad de habitaciones'
            }),
            'banos': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Cantidad de baños'
            }),
            'direccion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Dirección del inmueble'
            }),
            'region': forms.Select(attrs={
                'class': 'form-control'
            }),
            'comuna': forms.Select(attrs={
                'class': 'form-control'
            }),
            'tipo_inmueble': forms.Select(attrs={
                'class': 'form-control'
            }),
            'precio': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Precio del inmueble en CLP'
            }),
        }
        
