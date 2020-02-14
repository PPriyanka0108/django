from django.db import models

# Create your models here.

class Books_details(models.Model):
	book_name = models.CharField(max_length=30)
	email = models.EmailField()
	author = models.CharField(max_length=20)
	no_of_pages = models.IntegerField()




