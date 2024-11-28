from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import views as auth_views
from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm
from .forms import *
from .models import Inmueble




@login_required
def dashboard(request):
    return render (request, 'registration/dashboard.html', {'section':'dashboard'})

def inmuebles(request):
    inmuebles = Inmueble.objects.all()
    return render(request,'inmuebles.html',
                  {
                      'inmuebles':inmuebles
                  })

class CustomLogoutView(auth_views.LogoutView):
    next_page = 'login'
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
        return redirect(self.next_page)
    


def registrar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            messages.success(request, f'Bienvenido {usuario.nombre}')
            return redirect('register_done')
    else:
        form = UsuarioForm()
    
    return render(request, 'registration/register.html', {'form': form})

def register_done(request):
    return render(request, 'registration/register_done.html')


# def registro(request):
#     if request.method == 'POST':
#          form = UserCreationForm(request.POST)
#          if form.is_valid():
#              form.save()
#              return redirect('login')
#          else:
#              form = UserCreationForm()
#              return render(request, 'register.html', {'form': form})
