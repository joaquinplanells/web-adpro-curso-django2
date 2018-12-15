from django.contrib import admin
from .models import Project # ponemos el punto delante de models para referirnos al mismo directorio 'portfolio'

# Register your models here. El nombre 'ProjectAdmin' puede ser el que queramos.
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

# registramos el modelo 'Project' para que aparezca en el panel de administración.
admin.site.register(Project, ProjectAdmin)
