from rest_framework import serializers
from .models import Peserta

class PesertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Peserta
        fields = ['id', 'nama', 'npm', 'jurusan', 'instansi','mulai', 'akhir', 'status']



