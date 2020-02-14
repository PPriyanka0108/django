from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


# Create your views here.
from django.http import HttpResponse
from school_app.models import School, Student, Test, UserProfile

from school_app.forms import Studentform


def create_school(request):
	if request.method == 'POST':
		sch_obj = School(name=request.POST.get('name'))
		sch_obj.save()

	return render(request, 'create.html')


def create_student(request):
	school_obj = School.objects.all()
	if request.method == 'POST':
		#stu_obj = School.objects.get(id= request.POST.get('name'))
		st_obj = Student(student_name = request.POST.get('student_name'),
						 student_sec = request.POST.get('student_sec'),
						 student_roll_no = request.POST.get('student_roll_no'),
						 school_name = School.objects.get(id= request.POST.get('name')))
		st_obj.save()

	return render(request, 'create_student.html', {'school_obj':school_obj})


def create_test(request):
	msg=""
	if request.method == 'POST':
		test_obj=Studentform(request.POST)

		if test_obj.is_valid():
			test_clean = test_obj.cleaned_data
			t=Test(**test_clean)
			t.save()
			msg="created successfully"
	form=Studentform()
	return render(request, 'createform.html' , {'form':form,"msg":msg})


def registration(request):
	if request.method == 'POST':
		user_obj = UserProfile.objects.create_user(username=request.POST.get('username'),
								password=request.POST.get('password'),
								phone=request.POST.get('phone'),
								address=request.POST.get('address'))
		user_obj.save()
	return render(request,'registration.html')	


def login_view(request):
	msg=""
	if request.method=="POST":
		user=authenticate(username=request.POST.get("username"),
			          password=request.POST.get("password"))
		msg="login success"
		if user:

			return redirect("/home/")
			#msg="Welcome  to login !"
		else:
			msg="login fail"


	return render(request,'login.html',{"msg":msg})


def home_view(request):
	return render(request,"home.html")