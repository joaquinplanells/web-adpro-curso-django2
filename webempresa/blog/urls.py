
from django.urls import path
from . import views  # hace referencia al mismo directorio

urlpatterns = [
    path('', views.blog, name="blog"),

    # pasamos el identificador de la categoria utilizando '<category_id>/', este
    # es por defecto una cadena de caracteres y tenemos que forzar para que sea  
    # un número entero, para ello le ponemos delante int '<int:category_id>'
    path('category/<int:category_id>/', views.category, name="category")
]
