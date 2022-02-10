from rest_framework import serializers
from .models import Peserta, AbsencePeserta

class PesertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Peserta
        fields = ['id', 'nama', 'npm', 'jurusan', 'instansi','mulai', 'akhir', 'status']


class AbsenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbsencePeserta
        fields =['id','user_id', 'entrance_list', 'exit_list', 'isStarted', 'nth_absence', 'start_at']

