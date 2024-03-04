from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(AbstractUser):
    # cancel many to many questions
    groups = None
    user_permissions = None
    email = models.EmailField(max_length=255, unique=True, default='')
    gender = models.CharField(max_length=10)
    job = models.CharField(max_length=10)
    age = models.IntegerField()
    contact_num = models.CharField(max_length=20)
    user_type_data = ((1, "Admin"), (2, "User"))
    user_type = models.CharField(default=2, choices=user_type_data, max_length=10)

    r1feeling = models.CharField(max_length=10, null=True, default=None)
    r1score = models.FloatField(max_length=10, null=True, default=None)
    r2feeling = models.CharField(max_length=10, null=True, default=None)
    r2score = models.FloatField(max_length=10, null=True, default=None)


class TestUser(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    feeling = models.CharField(max_length=10, null=True, default=None)
    score = models.FloatField(max_length=10, null=True, default=None)
