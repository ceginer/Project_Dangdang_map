from distutils.command.upload import upload
from django.db import models

# Create your models here.

class User(models.Model):
    pass
    # 유저 부분 

class Location(models.Model):
    locationName = models.CharField(max_length=100)

class Cafe(models.Model):
    cafeName= models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    cafeAddress= models.CharField(max_length=100)
    cafePhone= models.CharField(max_length=100, null=True)
    cafeType= models.CharField(max_length=100, null=True)
    menuInfo = models.TextField(null=True)
    hourInfo = models.TextField(null=True)
    cafeLink1 = models.TextField(null=True)
    cafeDesc = models.TextField(null=True)
    cafeImg= models.ImageField(upload_to='', null=True)
    cafeMapx = models.CharField(max_length=100, null=True)
    cafeMapy = models.CharField(max_length=100, null=True)

class Place(models.Model):
    placeName = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    placeAddress = models.CharField(max_length=255)
    placePhone = models.CharField(max_length=100, null=True)
    placeStar = models.CharField(max_length=100, null=True)
    placeLink1 = models.TextField(null=True)
    placeLink2 = models.TextField(null=True)
    placeType = models.CharField(max_length=100, null=True)
    placeDesc = models.TextField(null=True)
    placeImg = models.ImageField(upload_to='', null=True)
    placeMapx = models.CharField(max_length=100, null=True)
    placeMapy = models.CharField(max_length=100, null=True)

class Accomodation(models.Model):
    accomodationName = models.CharField(max_length=100)
    # location = models.ForeignKey(Location, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    accomodationAddress = models.CharField(max_length=100)
    accomodationPhone = models.CharField(max_length=100, null=True)
    accomodationStar = models.CharField(max_length=100, null=True)
    accomodationLink1 = models.TextField(null=True)
    accomodationLink2 = models.TextField(null=True)
    accomodationType = models.CharField(max_length=100, null=True)
    accomodationDesc = models.CharField(max_length=255, null=True)
    accomodationImg = models.ImageField(upload_to='', null=True)
    accomodationMapx = models.CharField(max_length=100, null=True)
    accomodationMapy = models.CharField(max_length=100, null=True)

class Medical(models.Model):
    medicalName = models.CharField(max_length=100)
    medicalPhone = models.CharField(max_length=100)
    medicalAddress = models.CharField(max_length=100)
    medicalLocation = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

class Post(models.Model):
    postType = models.CharField(max_length=100)
    postGood= models.CharField(max_length=100)
    postBad= models.CharField(max_length=100)
    postImage= models.CharField(max_length=100)
    ranking= models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    cafe = models.ForeignKey(Accomodation, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)