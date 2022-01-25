from re import I
from .models import Peserta
from .serializers import PesertaSerializer
from rest_framework import viewsets
from django.http import FileResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
import pandas as pd



class PesertaViewSet(viewsets.ModelViewSet):
    queryset = Peserta.objects.all()
    serializer_class = PesertaSerializer
    # permission_classes = [IsAuthenticated]


class PesertaFileUpload(APIView):
    def read_file(self, file):
        data = pd.read_excel(file, engine="openpyxl")
        data.columns = ['id', 'nama', 'npm', 'jurusan','mulai', 'akhir', 'instansi', 'status']
        data_dict = data.to_dict("records")
        for i,data in enumerate(data_dict):
            data_dict[i]["mulai"] = str(data["mulai"]).split()[0]
            data_dict[i]["akhir"] = str(data["akhir"]).split()[0]
            data_dict[i]["status"] = True if data_dict[i]["status"].lower() == 'active' else False

        return data_dict

    def write_file(self, dict):
        df = pd.DataFrame.from_dict(dict)
        df.to_excel("./api/temp_file/peserta.xlsx")

    def post(self, request):
        excel_data = self.read_file(request.data['file'])
        serializer = PesertaSerializer(data=excel_data, many=True)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(status=status.HTTP_200_OK)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        peserta = Peserta.objects.all()
        serializer = PesertaSerializer(peserta, many=True)
        self.write_file(serializer.data)
        
        file = open("./api/temp_file/peserta.xlsx", 'rb')
        
        response = FileResponse(file)

        return response


class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        print(request.data)
        return Response(request.data, status=status.HTTP_200_OK)