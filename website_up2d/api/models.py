from email.policy import default
from pyexpat import model
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL
# Create your models here.
class Peserta(models.Model):
    nama = models.CharField(max_length=100)
    npm = models.CharField(max_length=100)
    jurusan = models.CharField(max_length=100)
    instansi = models.CharField(max_length=100)
    mulai = models.DateField()
    akhir = models.DateField()
    status = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-id']


class AbsencePeserta(models.Model):
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    entrance_list = models.CharField(max_length=50, default="0000000000000000000000000000000")
    exit_list = models.CharField(max_length=50, default="0000000000000000000000000000000")
    isStarted =models.BooleanField(default=False)
    nth_absence = models.IntegerField(default=1)
    start_at = models.CharField(max_length=100, default='')