from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path(
        '',
        TemplateView.as_view(template_name='home.html'),
        name='home',
    ),
    
    path(
        'about_us/',
        TemplateView.as_view(template_name='about_us.html'),
        name='about_us',
    ),
    
    path(
        'contact_us/',
        TemplateView.as_view(template_name='contact_us.html'),
        name='contact_us',
    ),
]

