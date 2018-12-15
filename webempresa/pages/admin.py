from django.contrib import admin
from .models import Page

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ("title", "order", "updated")

# registramos el modelo 'Page' para que aparezca en el panel de administración.
# admin.site.register(Modelo=Page, Class=PageAdmin)
admin.site.register(Page, PageAdmin)
