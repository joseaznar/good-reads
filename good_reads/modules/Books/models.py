from django.db import models
from modules.Authors.models import Author
from django.contrib.postgres.fields import ArrayField
#from modules.Users.models import *
from django.conf import settings

# Create your models here.
GENRE = (
        ("sf", "science fiction"),
        ("dr", "drama"),
        ("ft", "fantasy"),
        ("bg", "biography"),
        ("", ""),
        ("ot", "others"),
)


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    ISBN = models.CharField(max_length=18, unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date_published = models.DateField()
    cover_photo = models.URLField()
    summary = models.TextField()
    rating = models.DecimalField(decimal_places=2, max_digits=3)
    genre = models.CharField(max_length=80, choices=GENRE)
    tags = ArrayField(
        models.CharField(max_length=50),
        size=5
    )


class Coments(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    comment = models.TextField()
