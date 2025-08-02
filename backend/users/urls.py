from django.urls import path
from .views import (
    UserRegistrationView, UserProfileView, ChangePasswordView,
    CustomAuthToken, login_view, logout_view
)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('login-alt/', login_view, name='login-alt'),
    path('logout/', logout_view, name='logout'),
] 