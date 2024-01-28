from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)  # Change to CharField for storing phone numbers
    address = models.CharField(max_length=100)


