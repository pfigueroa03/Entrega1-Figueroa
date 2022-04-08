from django.contrib import admin

from .models import Editorial

# Register your models here.
class EditorialAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

admin.site.register(Editorial, EditorialAdmin)