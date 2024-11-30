from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
# from .views import registrar_usuario, register_done

urlpatterns = [
    
    path('', views.dashboard, name='dashboard'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.logout, name='logout'),
    
    
    path('accounts/register/', views.register, name='register'),
    path('accounts/register_done/', views.register_done, name='register_done'),
    

    
    
    path('inmuebles/', views.inmuebles, name='inmuebles'),
    path('mostrar_inmuebles/', views.mostrar_inmuebles, name='mostrar_inmuebles'),
    path('crear_inmueble/', views.crear_inmueble, name="crear_inmueble"),

    path('editar_inmueble/<int:inmueble_id>', views.detalle_inmueble, name="detalle_inmueble"),
    path('eliminar_inmueble/<int:id>/delete', views.eliminar_inmueble, name="eliminar_inmueble"),
    

    
]