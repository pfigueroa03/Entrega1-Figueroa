from django.contrib import admin

from .models import Autor

# Register your models here.
class AutorAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Autor, AutorAdmin)