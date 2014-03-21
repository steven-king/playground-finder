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
    Image = models.TextField

class Playground(models.Model):
    PlaygroundID = models.IntegerField(unique=True, null=False),
    Name = models.TextField,
    Street = models.TextField,
    Zipcode = models.IntegerField,
    Handicap = models.BooleanField,
    AgeID = models.IntegerField,
    SchoolDistrictID = models.IntegerField,
    Hours = models.TextField,
    isCertified = models.BooleanField,
    FeaturesID = models.IntegerField,
    Image = models.TextField,
    SafetyFeaturesID = models.IntegerField,
    TransportFeaturesID = models.IntegerField,
    GeoCoordinateLat = models.IntegerField,
    GeoCoordinateLon = models.IntegerField

class SchoolDistrict(models.Model):
    SchoolDistrictID = models.IntegerField(unique=True, null=False),
    DistrictName = models.TextField,
    ZipcodeStart = models.IntegerField,
    ZipcodeEnd = models.IntegerField,
    #I am not sure if we need GeoCoordinates or how to model them. Want to be able
    #to have the area on a map that a school district covers. GeoCodes the best way?
    GeoCoordinates = models.IntegerField

class Age(models.Model):
    AgeID = models.IntegerField(unique=True, null=False),
    ZeroTwo = models.BooleanField,
    TwoFour = models.BooleanField,
    FourSix = models.BooleanField,
    SixEight = models.BooleanField,
    EightTen = models.BooleanField,
    TenTwelve = models.BooleanField,
    TwelveFourteen = models.BooleanField

class School(models.Model):
    SchoolID = models.IntegerField(unique=True, null=False),
    Name = models.TextField,
    SchoolDistrictID = models.IntegerField(unique=False)

class UserReview(models.Model):
    ReviewID = models.IntegerField(unique=True, null=False),
    PlaygroundID = models.IntegerField(null=False),
    UserID = models.CharField(max_length=200),
    Stars = models.IntegerField,
    Review = models.CharField(max_length=1000)

class Features(models.Model):
    PlaygroundID = models.IntegerField(unique=True, null=False),
    Swing = models.IntegerField,
    Slide = models.IntegerField,
    MonkeyBars = models.IntegerField,
    SandBox = models.IntegerField,
    Field = models.IntegerField,
    PicnicTable = models.IntegerField,
    Bathrooms = models.IntegerField,
    ChangingStation = models.IntegerField,
    Shade = models.IntegerField,
    BasketballCourt = models.IntegerField,
    Baseball = models.IntegerField

class SafetyFeatures(models.Model):
    PlaygroundID = models.IntegerField(unique=True, null=False),
    ProximityToHighway = models.IntegerField,
    Fenced = models.BooleanField

class TransportationFeatures(models.Model):
    PlaygroundID = models.IntegerField(unique=True, null=False),
    BikePath = models.BooleanField,
    HikingTrail = models.BooleanField,
    AdjacentParking = models.BooleanField,
    NearbyParking = models.BooleanField,
    NoParking = models.BooleanField,
    ProximityToBus = models.IntegerField

class SuggestPlayground(models.Model):
    SuggestionID = models.IntegerField(unique=True, null=False),
    PlaygroundName = models.TextField,
    Address = models.TextField,
    Description = models.CharField(max_length=1000),
    Image = models.TextField