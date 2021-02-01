from django.urls import path, include
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.UserRegister, name='UserRegister'),
    path('accounts/', include('django.contrib.auth.urls'), name='login'),
    path('profile/', TemplateView.as_view(template_name='profile.html'), name='profile')
]