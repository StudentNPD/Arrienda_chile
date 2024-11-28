from django.contrib import admin
from django.urls import path, include        

urlpatterns = [
    path('admin-arrendado-gatos/', admin.site.urls),
    path('', include('gestion_inmuebles.urls'))
]
