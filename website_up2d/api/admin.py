from django.contrib import admin
from .models import Peserta, AbsencePeserta

class AdminAbsencePeserta(admin.ModelAdmin):
    list_display = ("id", "user", "entrance_list", "exit_list", "isStarted")


class AdminPeserta(admin.ModelAdmin):
    list_display = ("id", "nama", "npm", "jurusan")
    

admin.site.register(Peserta, AdminPeserta)
admin.site.register(AbsencePeserta, AdminAbsencePeserta)
