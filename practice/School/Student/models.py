from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student_Details(models.Model):
	st_name = models.CharField(max_length = 50)
	st_roll_no = models.IntegerField()
	st_sub = models.CharField(max_length = 10)
	st_image=models.ImageField(null=True, blank=True)

class User_Details(User):
	phone = models.CharField(max_length = 10)
                                   