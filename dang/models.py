from distutils.command.upload import upload
from django.db import models

# Create your models here.

class User(models.Model):
    pass
    # 유저 부분 

class Location(models.Model):
    locationName = models.CharField(max_length=100)

class Cafe(models.Model):
    name= models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    address= models.CharField(max_length=100)
    phone= models.CharField(max_length=100, null=True)
    type= models.CharField(max_length=100, null=True)
    menuInfo = models.TextField(null=True)
    hourInfo = models.TextField(null=True)
    link1 = models.TextField(null=True)
    desc = models.TextField(null=True)
    img= models.ImageField(upload_to='', null=True)
    mapx = models.CharField(max_length=100, null=True)
    mapy = models.CharField(max_length=100, null=True)

class Place(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=100, null=True)
    star = models.CharField(max_length=100, null=True)
    link1 = models.TextField(null=True)
    link2 = models.TextField(null=True)
    type = models.CharField(max_length=100, null=True)
    desc = models.TextField(null=True)
    img = models.ImageField(upload_to='', null=True)
    mapx = models.CharField(max_length=100, null=True)
    mapy = models.CharField(max_length=100, null=True)

class Accomodation(models.Model):
    name = models.CharField(max_length=100)
    # location = models.ForeignKey(Location, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, null=True)
    star = models.CharField(max_length=100, null=True)
    link1 = models.TextField(null=True)
    link2 = models.TextField(null=True)
    type = models.CharField(max_length=100, null=True)
    desc = models.CharField(max_length=255, null=True)
    img = models.ImageField(upload_to='', null=True)
    mapx = models.CharField(max_length=100, null=True)
    mapy = models.CharField(max_length=100, null=True)

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