from django.shortcuts import render, redirect
from Doctor.models import DoctorDetails, UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def create(request):
	# display_obj = DoctorDetails.objects.all()
	if request.method == 'POST':
		doc_obj = DoctorDetails(doc_name = request.POST.get('doc_name'),
			doc_specialization = request.POST.get('doc_specialization'),
			doc_qualification = request.POST.get('doc_qualification'))

		doc_obj.save()

		return redirect('/display/')

	return render(request, 'create.html')

def display(request):
	display_obj = DoctorDetails.objects.all()

	return render(request, 'display.html', {'display_obj':display_obj})

def update(request, id):
	up_obj =  DoctorDetails.objects.get(id=id)

	if request.method == 'POST':
		up_obj = DoctorDetails.objects.get(id=id)

		up_obj.doc_name = request.POST.get('doc_name')
		up_obj.doc_specialization = request.POST.get('doc_specialization')
		up_obj.doc_qualification = request.POST.get('doc_qualification')

		up_obj.save()
		return redirect('/display/')

	return render(request, 'update.html', {'up_obj': up_obj})

def registration(request):
	if request.method == 'POST':
		user = UserProfile.objects.create_user(username = request.POST.get('username'),
			password = request.POST.get('password'),
			email = request.POST.get('email'),
			phone = request.POST.get('phone'))

		user.save()

		# return redirect('/login/')

	return render(request, 'registration.html')

