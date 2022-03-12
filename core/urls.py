from django.urls import path
from core import views as core_views
from mainblog import views as mainblog_views

urlpatterns = [
    path('', core_views.pagina_inicio, name="Inicio"),
    path('about/', core_views.about_me, name = "Sobre" ),
    path('mainblog/', mainblog_views.proyectos, name = "Blog"),
    path('mainblog/proyectoFormulario/', mainblog_views.proyecto_formulario, name="ProyectoFormulario"),
    path('mainblog/autores/', mainblog_views.autores, name = "Autores"),
    path('mainblog/editoriales/', mainblog_views.editoriales, name="Editoriales"),
    path('mainblog/autor_form/', mainblog_views.formulario_autores, name = "AutoresFormulario"),
    path('mainblog/editorial_form/', mainblog_views.formulario_editorial, name = "EditorialFormulario"),
    path('mainblog/buscarProyecto/', mainblog_views.buscar_proyecto, name = "BuscarProyecto"),
    path('mainblog/buscar/', mainblog_views.buscar, name = "Buscar"),
]