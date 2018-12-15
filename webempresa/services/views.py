from django.shortcuts import render
from .models import Service

# Create your views here.
def services(request):
    list_services = Service.objects.all()# carga todos los registros del modelo 'Service'
    return render(request, "services/services.html", {'services':list_services })
