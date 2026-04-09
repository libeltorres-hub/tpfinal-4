from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from pages.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('pages/', include('pages.urls')),
    path('accounts/', include('accounts.urls')),
    path('mensajes/', include('mensajes.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)