"""photo_album URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from albums import views as view
from rest_framework.routers import Route, DefaultRouter
from django.contrib.auth import views as auth_views

router = DefaultRouter()
router.register(r'albums', view.AlbumViewSet)
router.register(r'photos', view.PhotoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view.index),
    path('details/', view.details),
    path('api-auth/', include('rest_framework.urls')),
    path('signup/', view.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

urlpatterns=urlpatterns+router.urls
