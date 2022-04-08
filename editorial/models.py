from django.db import models

# Create your models here.
class Editorial(models.Model):
    editorial_name = models.CharField(max_length = 50)
    location = models.CharField(max_length = 100)
    publication_date = models.DateField()
    created = models.DateTimeField(auto_now_add = True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now = True, verbose_name="Fecha de edicion")


    class Meta:
        verbose_name = "Editorial"
        verbose_name_plural = "Editoriales"
        ordering = ["-editorial_name"]
    
    def __str__(self):
        return self.editorial_name