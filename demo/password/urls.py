from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='generator'),
    path('password/', views.password, name='password'),
    path('about/', views.about, name='about'),
]
