
from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_participant = models.BooleanField(default=False)
    