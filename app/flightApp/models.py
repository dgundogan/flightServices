from django.db import models


# Create your models here.
class Flight(models.Model):
    flightNumber = models.CharField(max_length=10)
    operatingAirlines = models.CharField(max_length=20)
    departureCity = models.CharField(max_length=20)
    arrivalCity = models.CharField(max_length=20)
    dateOfDeparture = models.DateField()
    estimatedTimeOfDeparture = models.TimeField()


class Passenger(models.Model):
    firtname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    middleName = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=20)


class Reservation(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.OneToOneField(Passenger, on_delete=models.CASCADE)
