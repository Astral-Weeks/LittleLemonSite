from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from restaurant import views
from rest_framework.authtoken.views import obtain_auth_token
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns

router = routers.DefaultRouter()
# router.register(r'users', views.UsersView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('restaurant.urls')),
    path('', include(router.urls)),
    path('', include('django.contrib.auth.urls')),
    path('auth/users/', views.signup, name='sign-up'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('api-token-auth/', obtain_auth_token),
]

# urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
