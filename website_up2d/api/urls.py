from django.urls import path, include
from .views import  PesertaViewSet, PesertaFileUpload,  SertifikatPeserta, AbsenceParticipant
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register('peserta', PesertaViewSet, basename='peserta')



urlpatterns = [
    path('file/', PesertaFileUpload.as_view()),
    path('sertifikat/', SertifikatPeserta.as_view()),
    path('absence/', AbsenceParticipant.as_view()),
    path('absence/<int:id>', AbsenceParticipant.as_view()),
    path('', include(router.urls)),
]
