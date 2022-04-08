from django.db import models

# Create your models here.

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