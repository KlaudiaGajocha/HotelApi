from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.db.models.deletion import SET_NULL, PROTECT, CASCADE

 

class Attraction(models.Model):
    name = models.CharField(
        max_length = 128,
        null = False)

    price = models.DecimalField(
        max_digits=5, 
        decimal_places=2,
        null = True,
        default =1)

    description = models.TextField(
        null = True,
        default = "")

 

class Category(models.Model):
    cathegory_name = models.CharField(
        max_length = 128,
        null = False)

 


class Hotel(models.Model):
    name = models.CharField(
        max_length = 128,
        null = False)

    owner = models.CharField(
        max_length = 128,
        null = False)

    localization = models.CharField(
        max_length = 128)

 

    description = models.TextField(
        null = True,
        default = "")

    attractions = models.ManyToManyField(Attraction)

    category = models.ForeignKey(Category, on_delete= PROTECT)


class Rate(models.Model):
    value = models.IntegerField(validators=[MinValueValidator(1),
                                            MaxValueValidator(5),
                                            ])
    user = models.ForeignKey(User, on_delete = SET_NULL, null = True)
#    hotel = models.ForeignKey(Hotel)
    description = models.TextField(
        null = True,
        default = "")
    hotel = models.ForeignKey(Hotel, on_delete= CASCADE)

    def __str__(self):
        return self.name

