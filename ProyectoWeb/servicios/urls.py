from django.urls import path
from servicios.views import servicios
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [    
    path('', servicios, name="Servicios"),
]
