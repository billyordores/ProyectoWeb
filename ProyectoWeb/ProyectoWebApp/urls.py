from django.urls import path
from ProyectoWebApp.views import home, servicios, blog, contacto, tienda

urlpatterns = [
    path('', home, name="Home"),
    path('tienda/', tienda, name="Tienda"),
    path('servicios/', servicios, name="Servicios"),
    path('blog/', blog, name="Blog"),
    path('contacto/', contacto, name="Contacto"),
]