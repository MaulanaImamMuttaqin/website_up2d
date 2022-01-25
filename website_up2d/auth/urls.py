from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import MyObtainTokenPairView, RegisterView




urlpatterns = [
    path('token/obtain/', MyObtainTokenPairView.as_view(), name='token_create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
]