
from django.urls import path
from . import views  # hace referencia al mismo directorio

urlpatterns = [
    path('', views.contact, name="contact"),
]
