from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
# Create your models here.

AGE_LIMIT = (
    ("All","All"),
    ("Kid","Kid")
)

MOVIE_CHOICES = (
    ("seasonal","Seasonal"),
    ("single","Single"),
)


class CustomUser(AbstractUser):
    profiles = models.ManyToManyField("Profile",blank=True)



class Profile(models.Model):
    name = models.CharField(max_length=255)
    age_limit = models.CharField(choices=AGE_LIMIT,max_length=10)
    uuid = models.UUIDField(default=uuid.uuid4)

    def __str__(self) -> str:
        return self.name
    
    
class Movie(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    num_vol = models.CharField(choices=MOVIE_CHOICES,max_length=20)
    kind = models.CharField(max_length=255,default="")
    when = models.IntegerField(default=2023)
    length = models.CharField(max_length=255,default="1h35m")
    cast = models.CharField(max_length=255,default="Keanu Reeves")
    uuid = models.UUIDField(default=uuid.uuid4)
    image= models.ImageField(upload_to="Chon anh")
    age_limit = models.CharField(choices=AGE_LIMIT,max_length=10)
    video = models.ManyToManyField('Video')

    def __str__(self) -> str:
        return self.name


class Video(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to="movies")

    def __str__(self) -> str:
        return self.title





