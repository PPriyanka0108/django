from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class School(models.Model):
	name = models.CharField(max_length=25)

	def __str__(self):
		return self.name


class Student(models.Model):
	student_name = models.CharField(max_length=30)
	student_sec = models.CharField(max_length=10)
	student_roll_no = models.IntegerField()
	school_name = models.ForeignKey(School, on_delete=models.CASCADE)


class Test(models.Model):
	name=models.CharField(max_length=220)
	phone=models.CharField(max_length=220)
	email=models.EmailField()
	add=models.TextField()


class UserProfile(User):
	phone = models.CharField(max_length=10)
	address = models.CharField(max_length=30)

