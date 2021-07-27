from django.urls import path
from blog.views import  blog, categoria

urlpatterns = [
    path('', blog, name="Blog"),
    path('categoria/<int:categoria_id>/', categoria, name="categoria")
]
#esto es para poder ver la fotos en /admin
