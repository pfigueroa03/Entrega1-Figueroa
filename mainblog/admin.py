from django.contrib import admin
from .models import Project, Autor, PublishingCompany
# Register your models here.
class MainblogAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Project, MainblogAdmin)
admin.site.register(Autor, MainblogAdmin)
admin.site.register(PublishingCompany, MainblogAdmin)