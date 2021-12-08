from django.db import models

#izveidot tabulu visits

class StudentModel(models.Model):

    name = models.CharField(max_length=100)
    grades = models.CharField(max_length=100)
    average_grade = models.FloatField()
