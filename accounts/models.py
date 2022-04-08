from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)
    link = models.URLField(null=True)
    additional_description = models.CharField(max_length = 100)

    class Meta:
        verbose_name = "Avatar"
        verbose_name_plural = "Avatares"