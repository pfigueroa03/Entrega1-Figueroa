from django.db import models
from django import forms

# Create your models here.
class Project(models.Model):
    project_name = models.CharField(max_length=50)
    investigation_area = models.CharField(max_length=50)
    #images = models.ImageField(verbose_name = "Imagen", upload_to="mainblog")
    description = models.TextField(verbose_name="Cuerpo de su proyecto")
    created = models.DateTimeField(auto_now_add = True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now = True, verbose_name="Fecha de edicion")

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ["-created"]
    
    def __str__(self):
        return self.project_name

class Autor(models.Model):
    firstName = models.CharField(max_length = 50)
    lastName = models.CharField(max_length = 50)
    country = models.CharField(max_length = 50)
    created = models.DateTimeField(auto_now_add = True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now = True, verbose_name="Fecha de edicion")

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ["-lastName"]
    
    def __str__(self):
        return self.lastName

class PublishingCompany(models.Model):
    publishing_name = models.CharField(max_length = 50)
    location = models.CharField(max_length = 100)
    publication_date = models.DateField()
    created = models.DateTimeField(auto_now_add = True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now = True, verbose_name="Fecha de edicion")


    class Meta:
        verbose_name = "Editorial"
        verbose_name_plural = "Editoriales"
        ordering = ["-publishing_name"]
    
    def __str__(self):
        return self.publishing_name