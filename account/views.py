from django.contrib import admin
from django.shortcuts import render,redirect
from django.views.generic import ListView,CreateView
from django.http import HttpResponse
from .forms import *
from .models import *
from django.contrib.auth import authenticate,login
from django.views.decorators.http import require_POST
from django.urls import reverse
from django.conf import settings
from django.core.files.storage import FileSystemStorage

############### views are created here ###############

# login() view #

def login(request):
    name = Student.objects.all()
    context = {'name': name}
    if request.method =='POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        for itr in name:
            if itr.email == email and itr.password == password:
                return redirect('studdashboard',pk = itr.pk)

        Tpo = TPO.objects.all()
        for itr in Tpo:
            if itr.email == email and itr.password == password:
                return redirect('TPOdashboard',pk = itr.pk)

    else:
        name = LoginForm()
        context = {'name': name}
        return render(request,'registration/login.html',context)

# StudDashboardView() view #

def StudDashboardView(request,pk):
    stud_info = Student.objects.get(pk=pk)
    stud_data = StudentApplication.objects.filter(email=stud_info.email)
    context = {'stud_data':stud_data, 'stud_info':stud_info}
    return render(request,'student_dashboard.html',context)

# JobApplicationView() view #

def JobApplicationView(request,pk):
    stud_info = Student.objects.get(pk = pk)
    stud_data = StudentApplication.objects.filter(email = stud_info.email)
    form = JobApplicationForm(request.POST)
    context = {'stud_data':stud_data, 'stud_info':stud_info, 'form':form}
    if request.method == 'POST' and request.FILES['resume']: # file reference is retrieved from here #
        resume = request.FILES['resume']
        fs = FileSystemStorage(               # Default file Storage of Django #
            location = 'static/myfile'
        )
        filename = fs.save(resume.name,resume)
        uploaded_file_url = fs.url(filename)
        obj = StudentApplication()
        obj.status = 1
        obj.email = stud_info.email
        obj.company = request.POST.get('company')
        obj.position = request.POST.get('position')
        obj.resume = uploaded_file_url
        obj.reason_to_join = request.POST.get('reason_to_join')

        obj.save()
        return render(request,'student_dashboard.html',context)
    else:
        form = JobApplicationForm()
        return render(request,'job_application.html',context)

# TPODashboardView() view #

def TPODashboardView(request,pk):
    tpo_data = TPO.objects.get(pk = pk)
    stud_data = StudentApplication.objects.all()
    stud_info = Student.objects.all()
    context = {'stud_data':stud_data,'stud_info':stud_info,'tpo_data':tpo_data}
    return render(request, 'training_placement.html', context)

# ReviewJobApplicationView() view #

def ReviewJobApplicationView(request,pk):
    stud_info = StudentApplication.objects.get(pk = pk)
    stud_data = Student.objects.get(email=stud_info.email)
    form = JobApplicationReviewForm(request.POST)
    context = {'stud_data':stud_data,'stud_info':stud_info,'form':form}
    if request.method == "POST" and 'approve' in request.POST:
        stud_info.button = True
        stud_info.status = 4
        stud_info.save()
        stud_data = StudentApplication.objects.all()
        stud_info = Student.objects.all()
        context = {'stud_data':stud_data,'stud_info':stud_info}
        return render(request,'training_placement.html',context)
    elif request.method == 'POST' and 'reject' in request.POST:
        stud_info.status = 3
        stud_info.save()
        stud_data = StudentApplication.objects.all()
        stud_info = Student.objects.all()
        context = {'stud_data':stud_data,'stud_info':stud_info}
        return render(request,'training_placement.html',context)
    else:
        form = JobApplicationReviewForm()
        return render(request,'job_application_review.html',context)
