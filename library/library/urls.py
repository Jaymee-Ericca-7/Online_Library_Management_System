"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
#from . import views
from django.urls import path, include

from account.views import(registration_view, logout_view, login_view, profile, change_password)
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('account/', include('account.urls')),
    #path('account/', include('django.contrib.auth.urls')),
    path('register/', registration_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('library_system/', include('library_system.urls')),
    path('profile/', profile, name='profile'),
    path('password/', change_password, name='change_password')
]
#
# from django.views.generic import RedirectView
#
# urlpatterns += [
#     path('', RedirectView.as_view(url='library_system/', permanent=True)),
# ]
#
# from django.conf import settings
# from django.conf.urls.static import static
#
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
