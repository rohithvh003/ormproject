from django.db import models

# Create your models here.
class Student(models.Model):
    Sid = models.IntegerField()
    Sname = models.CharField(max_length=30)
    Smarks = models.FloatField()
    Sage = models.IntegerField()
    Sgender = models.CharField(max_length=20)
    Splace = models.CharField(max_length=30)

    def __str__(self):
        return self.Sname