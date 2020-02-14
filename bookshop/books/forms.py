from django import forms
from books.models import Books_details


class Bookform(forms.ModelForm):
	class Meta:
		model = Books_details
		fields = '__all__'
