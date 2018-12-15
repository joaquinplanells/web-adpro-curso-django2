from django.contrib import admin
from .models import Service

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

# registramos el modelo 'Service' para que aparezca en el panel de administración.
admin.site.register(Service, ServiceAdmin)  # admin.site.register(Modelo=Service, Class=ServiceAdmin)
