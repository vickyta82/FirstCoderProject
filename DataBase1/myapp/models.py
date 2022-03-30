from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField(primary_key=True)

class Student(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    id_number = models.IntegerField(primary_key=True)

class Professor(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    profession = models.CharField(max_length=50)
    id_number = models.IntegerField(primary_key=True)

class Paper(models.Model):
    name = models.CharField(max_length=60)
    submittion_date = models.DateField()
    submitted = models.BooleanField()




