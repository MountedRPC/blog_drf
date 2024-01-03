from django.urls import path

from .views import CustomTokenRefreshView, CustomTokenObtainPairView, RegisterUserView

urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('registrations/', RegisterUserView.as_view(), name='registrations'),
]