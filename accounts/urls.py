from django.urls import path

from accounts import views

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.login_request, name = "login"),
    path('signup/', views.register, name = 'register'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name = 'logout'),
    path('profile/', views.editarPerfil, name = "editar_perfil"),
    path('info_datos/', views.user_info, name="user_info")
]