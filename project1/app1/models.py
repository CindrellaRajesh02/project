from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=40)
    age = models.IntegerField()

    def __str__(self):
        return self.name
