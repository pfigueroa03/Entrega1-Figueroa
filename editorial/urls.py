from django.urls import path

from .views import EditorialList, EditorialDetalle, EditorialCreacion, EditorialUpdate, EditorialDelete

urlpatterns=[
    path('', EditorialList.as_view(), name='lista_editorial'),
    path(r'^(?<pk>\d+)$', EditorialDetalle.as_view(), name='detalle_editorial'),
    path(r'^nuevo$', EditorialCreacion.as_view(), name='crear_editorial'),
    path(r'^editar/(?P<pk>\d+)$', EditorialUpdate.as_view(), name='actualizar_editorial'),
    path(r'^borrar/(?P<pk>\d+)$', EditorialDelete.as_view(), name='eliminar_editorial'),
]