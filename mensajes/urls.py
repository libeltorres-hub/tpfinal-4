from django.urls import path
from . import views

urlpatterns = [
    path('', views.bandeja_entrada, name='bandeja-entrada'),
    path('enviados/', views.enviados, name='mensajes-enviados'),
    path('<int:pk>/', views.ver_mensaje, name='ver-mensaje'),
    path('nuevo/', views.enviar_mensaje, name='enviar-mensaje'),
    path('nuevo/<int:destinatario_id>/', views.enviar_mensaje, name='enviar-mensaje-a'),
]