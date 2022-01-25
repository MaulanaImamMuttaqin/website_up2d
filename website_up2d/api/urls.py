from django.urls import path, include
from .views import LoginView, PesertaViewSet, PesertaFileUpload, LoginView
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register('peserta', PesertaViewSet, basename='peserta')



urlpatterns = [
    path('file/', PesertaFileUpload.as_view()),
    path('login/', LoginView.as_view()),
    path('', include(router.urls)),
]
