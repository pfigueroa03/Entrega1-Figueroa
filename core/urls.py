from django.urls import path
from core import views as core_views
from mainblog import views as mainblog_views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', core_views.pagina_inicio, name="Inicio"),
    path('about-me/', core_views.about_me, name = "Sobre"),
    path('contact/', core_views.contact, name="Contacto"),
]