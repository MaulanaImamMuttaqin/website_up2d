from django.urls import path, re_path, include
from .views import AdminAppView
from django.views.generic.base import TemplateView
urlpatterns = [
    re_path('.*', TemplateView.as_view(template_name='index.html')),
]
