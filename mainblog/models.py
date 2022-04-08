from django.db import models
from django import forms

from ckeditor.fields import RichTextField

# Create your models here.
class Project(models.Model):
    project_name = models.CharField(max_length=50, verbose_name = "Titulo")
    subtitle = models.CharField(max_length=50, verbose_name = "Sub-Titulo")
    investigation_area = models.CharField(max_length=50, verbose_name = "Area de trabajo")
    summary = models.CharField(max_length=75, verbose_name = "Resumen")
    autor = models.CharField(max_length=50)
    images = models.ImageField(verbose_name = "Imagen", upload_to="mainblog")
    description = RichTextField(blank=True, null=True, verbose_name = "Descripcion")
    created = models.DateTimeField(auto_now_add = True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now = True, verbose_name="Fecha de edicion")

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ["-created"]
    
    def __str__(self):
        return self.project_name