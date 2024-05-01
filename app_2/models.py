from django.db import models

# Create your models here.
class Books(models.Model):
    name=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    price=models.IntegerField()
    pages=models.IntegerField()

    def __str__(self):
        return self.name
    
class Authors(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    books=models.ForeignKey(Books, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



