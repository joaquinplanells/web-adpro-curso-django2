from django.contrib import admin
from .models import Link

# Register your models here.
class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

    # los campos que no especifiquemos aqui se visualizan y se pueden modificar
    def get_readonly_fields(self, request, obj=None):
        # si el usuario pertenece al grupo 'Personal' solo se podra modificarar: ('url',)
        if request.user.groups.filter(name="Personal").exists():
            return ('key', 'name', 'created', 'updated')
        # si el usuario no pertenece al grupo 'Personal' solo se podra modificar: ('key', 'name', 'url')
        else:
            return ('created', 'updated')

# registramos el modelo 'Link' para que aparezca en el panel de administración.
# admin.site.register(Modelo=Link, Class=LinkAdmin)
admin.site.register(Link, LinkAdmin)
