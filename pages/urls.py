from django.urls import path
from . import views

urlpatterns = [
    path('', views.PageListView.as_view(), name='page-list'),
    path('<int:pk>/', views.PageDetailView.as_view(), name='page-detail'),
    path('crear/', views.PageCreateView.as_view(), name='page-create'),
    path('<int:pk>/editar/', views.page_edit, name='page-edit'),
    path('<int:pk>/borrar/', views.PageDeleteView.as_view(), name='page-delete'),
]
