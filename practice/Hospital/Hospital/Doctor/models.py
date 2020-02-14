from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class DoctorDetails(models.Model):
	doc_name = models.CharField(max_length = 50)
	doc_specialization = models.CharField(max_length = 50)
	doc_qualification = models.CharField(max_length = 20)


class UserProfile(User):
	phone = models.CharField(max_length = 10)
