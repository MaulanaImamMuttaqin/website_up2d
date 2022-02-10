from cProfile import label
from django.apps import AppConfig


class AuthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'auth'
    label = 'myauth' # pake label kalau misalkan nama app yang dipake sama dengan app bawaan django yang lain
