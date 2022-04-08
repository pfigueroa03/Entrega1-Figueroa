from django.urls import path

from accounts import views

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.login_request, name = "Login"),
    path('signup/', views.register, name = 'Register'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name = 'Logout'),
    path('profile/', views.editarPerfil, name = "EditarPerfil"),
    path('info_datos/', views.user_info, name="user_info")
]