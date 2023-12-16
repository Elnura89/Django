from django.db import models

# Create your models here.
class Students(models.Model):
    name=models.CharField(max_length=250)
    lastname=models.CharField(max_length=250)
    age=models.IntegerField()

    def __str__(self):
        return f'{self.name} {self.lastname}'
    
class Tech(models.Model):
    name=models.CharField(max_length=250)
    description=models.TextField()
   

    def __str__(self):
        return self.name
    
class Contacts(models.Model):
    fullname=models.CharField(null=False,blank=True,max_length=250)
    mail=models.CharField(null=False,blank=True,max_length=250)

    def __str__(self):
        return self.fullname