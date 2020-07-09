from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="libsys-home"),
    path('profile/', views.profile, name="libsys-profile"),
    path('about/',views.about, name="libsys-about"),
]
