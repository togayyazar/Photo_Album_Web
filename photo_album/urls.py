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
    path('shared/', view.shared_photo, name='shared_photo')
]

urlpatterns=urlpatterns+router.urls
