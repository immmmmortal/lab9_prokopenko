from django.db import models


# Create your models here.

class Hotel(models.Model):
    hotel_id = models.BigAutoField(primary_key=True)
    hotel_name = models.TextField()


class Guest(models.Model):
    guest_id = models.BigAutoField(primary_key=True)
    guest_name = models.TextField()
