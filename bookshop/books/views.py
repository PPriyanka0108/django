from django.shortcuts import render
from django.shortcuts import redirect

from .models import Books_details
from .forms import Bookform

# Create your views here.

def create(request):
	if request.method == 'POST':
		book_obj = Books_details(book_name=request.POST.get('b_book_name'),
			author = request.POST.get('b_author'),
			no_of_pages = request.POST.get('b_no_of_pages'))
		book_obj.save()

		return redirect('/display/')

	return render(request, 'create.html')

def display(request):
	display_obj = Books_details.objects.all()

	return render(request, 'display.html', {'display_obj':display_obj})

def create_bookform(request):
	if request.method == "POST":
		book_obj = Bookform(request.POST)

		if book_obj.is_valid():
			book_clean = book_obj.cleaned_data
			book_shop_obj = Books_details(**book_clean)
			book_shop_obj.save()
	form = Bookform()

	return render(request, 'createform_book.html', {'form':form})




