from django.urls import path

from .views import ProyectoList, ProyectoDetalle, ProyectoCreacion, ProyectoUpdate, ProyectoDelete#, buscar_proyecto

urlpatterns=[
    path('', ProyectoList.as_view(), name='lista_proyectos'),
    path(r'^(?<pk>\d+)$', ProyectoDetalle.as_view(), name='detalle_proyecto'),
    path(r'^nuevo$', ProyectoCreacion.as_view(), name='crear_proyecto'),
    path(r'^editar/(?P<pk>\d+)$', ProyectoUpdate.as_view(), name='actualizar_proyecto'),
    path(r'^borrar/(?P<pk>\d+)$', ProyectoDelete.as_view(), name='eliminar_proyecto'),
]


