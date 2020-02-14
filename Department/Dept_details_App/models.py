from django.db import models

# Create your models here.
class Student(models.Model):

	name=models.CharField(max_length = 50)
	

	def __str__(self):
		return self.name

class Dept(models.Model):
	dept_name = models.CharField(max_length = 50)
	Student=models.ForeignKey(Student,on_delete=models.CASCADE)
	dept_no = models.IntegerField()
	subject = models.CharField(max_length = 50)

