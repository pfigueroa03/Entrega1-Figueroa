from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import AutorList, AutorDetalle, AutorCreacion, AutorUpdate, AutorDelete, AutorDetail, AutorLista

urlpatterns=[
    path('', AutorList.as_view(), name='lista_autor'),
    path(r'^(?<pk>\d+)$', AutorDetalle.as_view(), name='detalle_autor'),
    path(r'^nuevo$', AutorCreacion.as_view(), name='crear_autor'),
    path(r'^editar/(?P<pk>\d+)$', AutorUpdate.as_view(), name='actualizar_autor'),
    path(r'^borrar/(?P<pk>\d+)$', AutorDelete.as_view(), name='eliminar_autor'),
    path('autor_api/', AutorLista.as_view(), name='lista_api_autor'),
    path('autor_api/<int:pk>', AutorDetail.as_view(), name='detalle_api_autor')
]

urlpatterns = format_suffix_patterns(urlpatterns)