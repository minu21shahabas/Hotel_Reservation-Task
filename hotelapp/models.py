from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class RoomCategory(models.Model):
    name=models.CharField(max_length=255)
    base_price=models.IntegerField()

class Room(models.Model):
    room_number=models.CharField(max_length=255)
    category=models.ForeignKey(RoomCategory,on_delete=models.CASCADE,null=True)
    is_available=models.BooleanField(default=True)

class Reservation(models.Model):
    room=models.ForeignKey(Room,on_delete=models.CASCADE,null=True)
    start_date=models.DateField()
    end_date=models.DateField()
    customer_name=models.CharField(max_length=255)
    total_price=models.IntegerField()

class SpecialRate(models.Model):
    room_category=models.ForeignKey(RoomCategory,on_delete=models.CASCADE,null=True)
    start_date=models.DateField()
    end_date=models.DateField()
    rate_multiplier=models.IntegerField()