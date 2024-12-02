from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth import views as auth_views
from django.contrib import messages

from .forms import *
from .models import *




@login_required
def dashboard(request):
    return render (request, 'layouts/dashboard.html', {'section':'dashboard'})

def inmuebles(request):
    inmuebles = Inmueble.objects.all()
    comunas = Comuna.objects.all()
    regiones = Region.objects.all()
    
    region_id = request.POST.get('region')
    comuna_id = request.POST.get('comuna')
    tipo_inmueble = request.POST.get('tipo_inmueble')
    
    if comuna_id and comuna_id != '':
        inmuebles = inmuebles.filter(comuna_id=comuna_id)
    elif region_id and region_id != '':
        inmuebles = inmuebles.filter(region_id=region_id)
    elif tipo_inmueble :
        inmuebles = inmuebles.filter(tipo_inmueble=tipo_inmueble)
    
    context = { 
        'inmuebles' :inmuebles,
        'comunas' :comunas,
        'regiones':regiones,
        'tipo_inmueble':tipo_inmueble,
        'comuna_seleccionada': None
    }

    return render(request,'inmuebles.html', context)
    
@login_required
def crear_inmueble(request):
    if request.method == 'GET':
        return render(request, 'crear_inmueble.html',{
            'form': InmuebleForm
        })
    else:
        try:
            form = InmuebleForm(request.POST, request.FILES)
            if form.is_valid():
                nuevo_inmueble = form.save(commit=False)
                nuevo_inmueble.usuario = request.user
                nuevo_inmueble.save()
                return redirect('inmuebles')
            else:
                raise ValueError('Formulario inválido')
        except ValueError:
            return render(request, 'crear_inmueble.html',{
                'form': InmuebleForm,
                'error': ' Ingresa datos validos'
            })

@login_required
def detalle_inmueble(request, inmueble_id):
    inmueble = get_object_or_404(Inmueble, pk=inmueble_id, usuario=request.user)
    if request.method == 'POST':
        form = InmuebleForm(request.POST, request.FILES, instance=inmueble)
        if form.is_valid():
            form.save()
            messages.success(request, 'Propiedad actualizada exitosamente.')
            return redirect('inmuebles')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = InmuebleForm(instance=inmueble)
    
    return render(request, 'editar_inmueble.html', {
        'form': form,
        'inmueble': inmueble
    })


@login_required
def eliminar_inmueble(request, inmueble_id):
    inmueble = get_object_or_404(Inmueble, pk=inmueble_id)
    inmueble.delete()
    messages.success(request, 'Propiedad eliminada exitosamente.')
    return redirect('inmuebles')

    
@login_required
def mostrar_inmuebles(request):
    mostrar_inmuebles = Inmueble.objects.filter(
        usuario = request.user
    )
    return render(request, 'mostrar_inmuebles.html', {
        'mostrar_inmuebles': mostrar_inmuebles
    }) 


@login_required
def editar_perfil(request):
    user = request.user
    form = UsuarioForm(request.POST or None, request.FILES or None, instance=user)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('inmuebles')

    context = {
        "form": form
    }

    return render(request, "editar_perfil.html", context)

def register(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            authenticated_user = authenticate(
                username=form.cleaned_data['email'], 
                password=form.cleaned_data['password1']
            )
            if authenticated_user:
                login(request, authenticated_user)
                return redirect('inmuebles') 
    else:
        form = UsuarioForm()
    
    return render(request, 'registration/register.html', {'form': form})
  

