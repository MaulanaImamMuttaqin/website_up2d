from pyexpat import model
from django.db import models

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

    def __str__(self):
        return self.nama