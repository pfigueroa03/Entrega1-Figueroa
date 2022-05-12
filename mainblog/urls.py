from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import ProyectoList, ProyectoDetalle, ProyectoCreacion, ProyectoUpdate, ProyectoDelete, ProjectList, ProjectDetail

urlpatterns=[
    path('', ProyectoList.as_view(), name='lista_proyectos'),
    path(r'^(?<pk>\d+)$', ProyectoDetalle.as_view(), name='detalle_proyecto'),
    path(r'^nuevo$', ProyectoCreacion.as_view(), name='crear_proyecto'),
    path(r'^editar/(?P<pk>\d+)$', ProyectoUpdate.as_view(), name='actualizar_proyecto'),
    path(r'^borrar/(?P<pk>\d+)$', ProyectoDelete.as_view(), name='eliminar_proyecto'),
    path('projects_api/', ProjectList.as_view(), name="lista_api_proyectos"),
    path('projects_api/<int:pk>', ProjectDetail.as_view(), name='detalle_api_proyectos'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

