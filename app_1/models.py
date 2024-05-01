from django.db import models

# 
class Universitate(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    def __str__(self):
        return self.name


class Fakultet (models.Model):

    name = models.CharField(max_length=100)
    universitet = models.ForeignKey(Universitate, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.name

class Guruh(models.Model):

    name = models.CharField(max_length=100, blank=True, null=True)
    fakultet = models.ForeignKey(Fakultet, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.name



class Kafedra(models.Model):

    name = models.CharField(max_length=100)
    universitet = models.ForeignKey(Universitate, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

class Fan(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Ustoz (models.Model):
    name = models.CharField(max_length=100)
    kafedra = models.ForeignKey(Kafedra, models.DO_NOTHING)
    def __str__(self):
        return f"{self.name} {self.kafedra}"


class Student (models.Model):
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    universitet = models.ForeignKey(Universitate, null=True, on_delete=models.SET_NULL)
    fakultet = models.ForeignKey(Fakultet, null=True, on_delete=models.SET_NULL)
    guruh = models.ForeignKey(Guruh, null=True, on_delete=models.SET_NULL)
    fan = models.ForeignKey(Fan, null=True, on_delete=models.SET_NULL)
    ustoz = models.ForeignKey(Ustoz, null=True, on_delete=models.SET_NULL)

    def __str__(self):
         return f"{self.first_name} {self.last_name}"
