from django.urls import path
from .views import RegisterView,CustomLoginView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='custom_login'),

    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
