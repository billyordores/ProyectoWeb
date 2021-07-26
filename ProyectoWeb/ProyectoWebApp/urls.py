from django.urls import path
from ProyectoWebApp.views import home, contacto, tienda
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name="Home"),
    path('tienda/', tienda, name="Tienda"),
    path('contacto/', contacto, name="Contacto"),
]
#esto es para poder ver la fotos en /admin
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 