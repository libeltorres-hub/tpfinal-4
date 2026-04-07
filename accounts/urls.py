from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registro/', views.signup, name='signup'),
    path('perfil/', views.profile, name='profile'),
    path('perfil/editar/', views.profile_edit, name='profile-edit'),
    path('contrasena/', views.password_change_view, name='password-change'),
]
