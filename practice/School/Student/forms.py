from django import forms
from .models import Student_Details

class Student_Form(forms.ModelForm):
	class Meta:
		model=Student_Details
		fields='__all__'
