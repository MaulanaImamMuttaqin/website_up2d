from rest_framework import serializers

from .models import Peserta, AbsencePeserta
from auth.models import CustomUser
from auth.serializers import RegisterSerializer

class PesertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Peserta
        fields = ['id', 'nama', 'npm', 'jurusan', 'instansi','mulai', 'akhir', 'status']


class AbsenceSerializer(serializers.ModelSerializer):
    user = RegisterSerializer(required=True)
    class Meta:
        model = AbsencePeserta
        fields =['id','user_id', 'entrance_list', 'exit_list', 'isStarted', 'nth_absence', 'start_at', 'finish_at', 'user']

    def create(self, validated_data):
        user = validated_data.pop('user')
        user = RegisterSerializer.create(RegisterSerializer(), validated_data=user)
        absence = AbsencePeserta.objects.create(user=user, start_at=validated_data.pop("start_at"), finish_at=validated_data.pop("finish_at") )

        return absence
