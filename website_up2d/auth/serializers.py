from email.policy import default
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


User = get_user_model()

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['name'] = f'{user.first_name} {user.last_name}' 
        token['role_id'] = 1 if user.is_admin else 2
        return token

class RegisterSerializer(serializers.ModelSerializer):
    #buat memvalidasi data yang dikirim dari client ke server, udah cocok belum sama yang dibuat di bawah 
    # email = serializers.EmailField(
    #         required=False,
    #         validators=[UniqueValidator(queryset=User.objects.all())]
    #         )
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    #sampai sini

    class Meta:
        model = User
        # Fields field shows which fields from the Model class to show in your new Form.
        fields = ('username', 'password', 'password2', 'first_name', 'last_name', 'is_admin', 'is_participant', 'is_staff')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        # data yang mau dimasukin ke database user
        user = User.objects.create(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            is_admin=validated_data['is_admin'],
            is_participant=validated_data['is_participant'],
            is_staff=validated_data['is_staff']
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user