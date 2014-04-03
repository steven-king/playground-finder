from django.db import models

# Create your models here.
class User(models.Model):
    UserID = models.CharField(unique=True, null=False, max_length=200),
    Name = models.CharField(null=False),
    Description = models.TextField,
    Zipcode = models.IntegerField,
    Age = models.IntegerField,
    isWorkingMom = models.BooleanField,
    isWorkingDad = models.BooleanField,
    isStayMom = models.BooleanField,
    isStayDad = models.BooleanField,
    isGrandma = models.BooleanField,
    isOther = models.BooleanField,
    FavoritesID = models.IntegerField,
    Image = models.TextField,