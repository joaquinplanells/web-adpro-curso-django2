from django.urls import path
from . import views  # hace referencia al mismo directorio

urlpatterns = [
    # pasamos el identificador de la página utilizando '<page_id>/'
    # <page_id> es por defecto una cadena de caracteres y tenemos que forzar para que sea un
    #           número entero, para ello le ponemos delante int '<int:page_id>'
    # <slug:page_slug> definimos un tercer parámetro para el slug
    path('<int:page_id>/<slug:page_slug>/', views.page, name="page")
]
