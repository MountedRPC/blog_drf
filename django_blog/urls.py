from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework import routers

from accounts import views as accounts_views

router = routers.DefaultRouter()
router.register('accounts', accounts_views.UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('auth_user.urls'), name='auth_user'),
    path('api/v1/', include(router.urls)),

    # Documentation
    path('docs/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
