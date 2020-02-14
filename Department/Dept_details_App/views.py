from django.shortcuts import render

from Dept_details_App.models import Dept,Student
from django.shortcuts import redirect
# Create your views here.
def create_dept(request):
	st=Student.objects.all()

	if request.method =="POST":
		#import pdb; pdb.set_trace()
		st=Student.objects.get(id=request.POST.get('name'))
		#import pdb; pdb.set_trace()
		
		dept_obj = Dept(dept_name=request.POST.get('dept_name'), 
			            Student=st,
			 			dept_no=request.POST.get('dept_no'),
			 			subject=request.POST.get('sub'))
		dept_obj.save()

		return redirect('/list/')


	return render (request, 'dept_list.html',{'st':st})


def get_data(request):
	d_list=Dept.objects.all()
	return render (request,'get_data.html',{'d_list':d_list})


def update_list(request,id):
	d_obj=Dept.objects.get(id=id)
	if request.method=="POST":
		d_obj=Dept.objects.get(id=id)
		d_obj.dept_name=request.POST.get('dept_name')
		d_obj.dept_no=request.POST.get('dept_no')
		d_obj.subject=request.POST.get('sub')
		d_obj.save()

	return render (request,'update.html',{"d_obj":d_obj,"msg":"successfully updated"})

def delete_list(request, id):
	obj_del = Dept.objects.get(id=id)
	obj_del.delete()

	return redirect('/list/')
