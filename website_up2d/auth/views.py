
from django.shortcuts import render
from .serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer
from api.serializers import AbsenceSerializer
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

User = get_user_model()
class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = RegisterSerializer

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     obj = serializer.save()
    #     return obj

    # def post(self, request, *args, **kwargs):
    #     data = {
    #         "start_at" : request.data["start_at"]
    #     }
        
    #     try:
    #         self.create(request, *args, **kwargs)
    #         return Response(request.data, status=status.HTTP_200_OK)

    #     except Exception as e:
    #         print(e)
    #         return Response({"error" : str(e)}, status=status.HTTP_200_OK)