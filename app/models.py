from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Home(models.Model):
    movies=models.CharField(max_length=100)
    slot=models.CharField(max_length=200,blank=True,null=True)

    def __str__(self):
        return str(self.id)

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=12, default=None)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    zipcode = models.IntegerField()

    def __str__(self):
        return str(self.id)

class BookTicket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slot = models.CharField(max_length=200)
    seats = models.PositiveIntegerField(default=1)
    category_of_seats = models.CharField(max_length=10)
    book = models.BooleanField()
    delete = models.BooleanField()

    def __str__(self):
        return str(self.user.username)