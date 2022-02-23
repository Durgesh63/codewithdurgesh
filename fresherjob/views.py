from django.shortcuts import render,HttpResponseRedirect
from .models import Fresherjob,jovvacancies
from django.contrib import messages
import re
# Create your views here.

def fresherjob(request):
    return render(request,'fresherjob/fresherhomepage.html',{'current_path': request.build_absolute_uri()})

def freshercontent(request):
    return render(request,'fresherjob/fresherjobcontent.html',{'current_path': request.build_absolute_uri()})

def postjob(request):
    if request.method == "POST":
        email = request.POST['email']
        companyname = request.POST['companyname']
        locations = request.POST['locations']
        role_name = request.POST['role_name']
        experience = request.POST['experience']
        qualifications = request.POST['qualifications']
        application_link = request.POST['application_link']
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(regex, email) and len(locations) > 0 and len(companyname) > 0 and len(email) > 5 and len(role_name) > 0 and len(experience) > 0 and len(qualifications) > 0:
            jovvacancies.objects.create(email=email,company=companyname,location=locations,role_name=role_name,job_experience=experience,qualifications=qualifications,application_link=application_link)
            messages.success(request,f"Succefully Job Vacancies save. Thankyou for Contribution.")
            return HttpResponseRedirect('/fresher-job/post-job-vacancies/')
        else:
            messages.error(request,f"Please enter a full informations .Note that every fields may be case-sensitive and filled.")
    return render(request,'fresherjob/postjob.html',{'current_path': request.build_absolute_uri()})


def contents(request,slug):
    content_data = Fresherjob.objects.get(slug=slug , publish="publish")
    return render(request,'fresherjob/contents.html',{"data":content_data,'current_path': request.build_absolute_uri()})

def editor(request,slug):
    if request.user.is_authenticated:
        content_data = Fresherjob.objects.get(slug=slug)
        return render(request,'fresherjob/editorpost.html',{"data":content_data ,'current_path': request.build_absolute_uri()})
    else:
        return HttpResponseRedirect('/login/')