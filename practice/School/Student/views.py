from django.shortcuts import render, redirect
from Student.models import Student_Details, User_Details
from Student.forms import Student_Form
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def create(request):
	if request.method == 'POST':
		st_obj = Student_Details(st_name=request.POST.get('st_name'),
			st_roll_no = request.POST.get('st_roll_no'),
			st_sub = request.POST.get('st_sub'))
		st_obj.save()

		return redirect('/display/')

	return render(request, 'create.html')


@login_required(login_url="login")
def display(request):
	st_display = Student_Details.objects.all()

	return render(request, 'display.html', {'st_display': st_display})


@login_required(login_url="login")
def update(request, id):
	st_update = Student_Details.objects.get(id=id)

	if request.method=='POST':
		st_update = Student_Details.objects.get(id=id)

		st_update.st_name = request.POST.get('st_name')
		st_update.st_roll_no = request.POST.get('st_roll_no')
		st_update.st_sub = request.POST.get('st_sub')

		st_update.save()

		return redirect('/display/')

	return render(request, 'update.html', {'st_update': st_update})


@login_required(login_url="login")	
def delete(request, id):
	st_del = Student_Details.objects.get(id=id)
	# if request.method=='POST':
	#	st_del = Student_Details.objects.get(id=id)
	st_del.delete()
	return redirect('/display/')	

	# return render(request, 'delete.html',{"st_del":st_del})


def create_form(request):
	form = Student_Form()
	if request.method == 'POST':
		form_obj = Student_Form(request.POST)

		if form_obj.is_valid():
			
			form_obj.save()

			return redirect('/display/')
		
	return render(request, 'create_form.html', {'form':form})		


def update_form(request,id):
	up_obj = Student_Details.objects.get(id=id)
	print(up_obj)
	if request.method == 'POST':
		up_form = Student_Form(request.POST, instance=up_obj)
		if up_form.is_valid():
			up_form.save()
			
			return redirect('/display/')

	form = Student_Form(instance=up_obj)

	return render(request, 'create_form.html', {'form':form})


def registration(request):
	if request.method == 'POST':
		user = User_Details.objects.create_user(username = request.POST.get('username'),
			password = request.POST.get('password'),
			email = request.POST.get('email'),
			phone = request.POST.get('phone'))

		user.save()

		return redirect('/login/')

	return render(request, 'registration.html')


def login_view(request):
	if request.method == 'POST':
		validate_obj = authenticate(username = request.POST.get('username'),
			password = request.POST.get('password'),
			email = request.POST.get('email'),
			phone = request.POST.get('phone'))

		if validate_obj:
			#return render(request, 'login_success.html')
			login(request, validate_obj)
			return redirect('/create/')
		else:
			return render(request, 'login.html')
	return render(request, 'login.html')


def signout(request):
	if request.method == 'POST':
		logout(request)

		return redirect('/login/')
	return render(request, 'logout.html')


def create_form_img(request):
	form = Student_Form()
	if request.method == 'POST':
		form_obj = Student_Form(request.POST,request.FILES)

		if form_obj.is_valid():
			
			form_obj.save()

			return redirect('/display/')
		
	return render(request, 'create_form_img.html', {'form':form})		
