from django.db import models

# Create your models here.

GENDER = (
    ("M", "Masculino"),
    ("F", "Femenino"),
)


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=50)
    biography = models.TextField()
    gender = models.CharField(max_length=20, choices=GENDER)
    age = models.IntegerField(max_length=3)
    is_alive = models.BooleanField(default=True)

    def __str__(self):
        return self.name
