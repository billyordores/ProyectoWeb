from django.urls import path
from blog.views import  blog

urlpatterns = [
    path('', blog, name="Blog"),
]
#esto es para poder ver la fotos en /admin
