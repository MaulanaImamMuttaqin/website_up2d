from .models import  Peserta, AbsencePeserta
from .serializers import  PesertaSerializer, AbsenceSerializer
from rest_framework import viewsets
from django.http import FileResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
import pandas as pd
from bs4 import BeautifulSoup
from math import ceil
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
from datetime import date, datetime
from operator import itemgetter
from time import time

class PesertaViewSet(viewsets.ModelViewSet):
    queryset = Peserta.objects.all()
    serializer_class = PesertaSerializer
    permission_classes = [IsAuthenticated]


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

class SertifikatPeserta(APIView):
    def generate_svg(self, data):
        svg = BeautifulSoup(open('./api/temp_file/sertifikat/sertifikat.svg'), 'xml')
        for key, value in data.items():
            if key == 'alamat':
                alamat_len = len(value)
                al = value.split()
                print(alamat_len)
                if alamat_len > 55:
                    first, second = al[:ceil(len(al)/2)], al[ceil(len(al)/2):]
                    svg.find(id='alamat').contents[0].replace_with(" ".join(first))
                    svg.find(id='alamat2').contents[0].replace_with(" ".join(second))
                else:
                    svg.find(id='alamat').contents[0].replace_with(value)
            else:
                if key:
                    svg.find(id=key).contents[0].replace_with(value)


        with open('./api/temp_file/sertifikat/sertifikatbaru.svg', 'w') as file:
            file.write(str(svg))

    def convert_svg_to_png(self):
        drawing = svg2rlg('./api/temp_file/sertifikat/sertifikatbaru.svg')
        renderPM.drawToFile(drawing, './api/temp_file/sertifikat/sertifikatbaru.png', fmt='PNG')
        return True

    def post(self, request):
        print(request.data)
        self.generate_svg(request.data)
        if self.convert_svg_to_png():
            file = open("./api/temp_file/sertifikat/sertifikatbaru.png", 'rb')
            response = FileResponse(file, as_attachment=True, filename="sertifikatbaru.png")
            return response
        
        return Response(status=status.HTTP_400_BAD_REQUEST)


class AbsenceParticipant(APIView):
    permission_classes = (IsAuthenticated,)
    

    def post(self, request):
        serializer = AbsenceSerializer(data= request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response({"data" : serializer.error_messages}, status= status.HTTP_200_OK)


    def patch(self, request):
        id, absence, list, types, start_at = itemgetter('id', 'absence', 'list', 'types', 'start_at')(request.data)

        
        data = {}

        if int(time()) > int(start_at) :
            days = int((int(time()+25200) - int(start_at))/86400)
            data['nth_absence'] =  days + 1

        if types == 1:
            data['entrance_list'] = list[:absence-1] + str(1) + list[absence:]
        else:
            data['exit_list'] = list[:absence-1] + str(1) + list[absence:]


        absensi = AbsencePeserta.objects.get(user_id=id)
        serializer = AbsenceSerializer(absensi, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            print(id, absence, list, types)
            return Response({"status": True}, status=status.HTTP_200_OK)

        return Response({"status": False}, status=status.HTTP_406_NOT_ACCEPTABLE)
    
    def get(self, request, id):
        absensi = AbsencePeserta.objects.get(user_id=id)
        serializer = AbsenceSerializer(absensi)
        now = datetime.now()
        data = serializer.data
        print(data)
        data.update({
            "date" :  str(date.today().strftime("%A, %d %B %Y")),
            "isStarted" : True if int(time()+25200) > int(data["start_at"]) else False,
            "types" :  1 if 8 <= now.hour < 9  else 3 if 16 <= now.hour < 17 else 2,
            "day_type" : '',
            "isFinished": False if int(time()+25200) > int(data["finish_at"]) else True
        })

        if int(time()+25200) > int(data["start_at"]) :
            days = int((int(time()+25200) - int(data["start_at"]))/86400)
            data['nth_absence'] =  days + 1
        print(data)
        if data['types'] == 1 :
            data["status"] = data["entrance_list"][data['nth_absence']-1]
        else :
            data["status"] = data["exit_list"][data['nth_absence']-1]

        print(data)
        return Response(data, status=status.HTTP_200_OK )
