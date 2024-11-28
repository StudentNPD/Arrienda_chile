from django import forms 
from django.contrib.auth.models import User
from .models import Usuario


# class LoginForm(forms.Form):
#     username = forms.CharField(
#         max_length=150,
#         widget=forms.TextInput(
#         #     attrs={
#         #     'class': 'form-control',
#         #     'placeholder': 'Ingrese su nombre de usuario'
#         # }
#             )
#     )
#     password = forms.CharField(
#         widget=forms.PasswordInput(
#             # attrs={
#             # 'class': 'form-control',
#             # 'placeholder': 'Ingrese su contraseña'}
#         )
#     )
    
    # def _init_(self, *args, **kwargs):
    #     super()._init_(*args, **kwargs)
    #     self.fields['username'].widget.attrs['class'] = 'form-control'
    #     self.fields['username'].widget.attrs['placeholder'] = 'usuario'
    #     self.fields['password'].widget.attrs['class'] = 'form-control'
    #     self.fields['password'].widget.attrs['placeholder'] = 'contraseña'

    
class UsuarioForm(forms.ModelForm):
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
            'tipo_usuario'
        ]
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
                    'placeholder': 'Nombre',
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Direccion',
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Telefono',
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Email',
                }
            )
            
            
        }