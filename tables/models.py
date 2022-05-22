from django.db import models


# Create your models here.

class Student(models.Model):
    student_id = models.BigAutoField(primary_key=True)
    student_name = models.TextField()


class Teacher(models.Model):
    teacher_id = models.BigAutoField(primary_key=True)
    teacher_name = models.TextField()
