from django.urls import path

from .views import AutorList, AutorDetalle, AutorCreacion, AutorUpdate, AutorDelete

urlpatterns=[
    path('', AutorList.as_view(), name='lista_autor'),
    path(r'^(?<pk>\d+)$', AutorDetalle.as_view(), name='detalle_autor'),
    path(r'^nuevo$', AutorCreacion.as_view(), name='crear_autor'),
    path(r'^editar/(?P<pk>\d+)$', AutorUpdate.as_view(), name='actualizar_autor'),
    path(r'^borrar/(?P<pk>\d+)$', AutorDelete.as_view(), name='eliminar_autor'),
]