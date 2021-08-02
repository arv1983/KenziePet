from django.db import models

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=255)
    scientific_name = models.CharField(max_length=255)

    # testar
    def __str__(self):
        return f"{self.name} - {self.scientific_name}"

class Characteristic(models.Model):
    name = models.CharField(max_length=255)

    # testar
    def __str__(self):
        return f"{self.name}"

class Animal(models.Model):
    name = models.CharField(max_length=255)
    age = models.FloatField()
    weight = models.FloatField()
    sex = models.CharField(max_length=1)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    Characteristic = models.ManyToManyField(Characteristic)

    def __str__(self):
        return f"{self.name} - {self.age} - {self.weight} - {self.sex}"
