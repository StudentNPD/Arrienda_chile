from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import registrar_usuario, register_done

urlpatterns = [
    
    path('', views.dashboard, name='dashboard'),
    
    path('login/', auth_views.LoginView.as_view(
        template_name='registration/login.html',
        redirect_authenticated_user=True
    ), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('register/', registrar_usuario, name='register'),
    path('registration/register_done/', register_done, name='register_done'),
    
    path('inmuebles/', views.inmuebles, name='inmuebles'),
    # path('register/', register, name='register'),
    # path('register/', registro, name='register'),
    #path('login/', auth_views.LoginView.as_view(),name='login'),
    #path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
]