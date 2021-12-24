# base
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from . import views
from .views import BlogHomeView

urlpatterns = [
    path('artikel/', include('artikel.urls', namespace='artikel')),
    path('', BlogHomeView.as_view(template_name='index.html'), name='home'),
    path('admin/', admin.site.urls),
]
