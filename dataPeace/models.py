from django.db import models

class Student(models.Model):

    first_name =  models.CharField(max_length=50);
    last_name = models.CharField(max_length=50);
    company_name = models.CharField(max_length=50);
    city = models.CharField(max_length=50);
    state = models.CharField(max_length=50);
    zip = models.CharField(max_length=50);
    email = models.CharField(max_length=50);
    web = models.CharField(max_length=500);
    age = models.IntegerField();

    def __str__(self):
        return self.first_name


