from django.urls import path
from .views import RegisterView,CustomLoginView,UserListView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='custom_login'),
      path('users/', UserListView.as_view(), name='user_list'), 

    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
