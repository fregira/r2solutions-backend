# accounts/urls.py
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('dashboard-stats/', views.dashboard_stats, name='dashboard_stats'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('health/', views.health_check, name='health_check'),
]