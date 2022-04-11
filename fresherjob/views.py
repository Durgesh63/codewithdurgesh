import json
from django.http import HttpResponse
from django.shortcuts import render,HttpResponseRedirect
from .models import Fresherjob,jovvacancies,jobcommments
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
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


@csrf_exempt
def comments(request):
    if request.method == "POST" and request.is_ajax:
        slug = request.POST['slug']
        comment = request.POST['comment']
        email = request.POST['email']
        name = request.POST['name']
        api = request.POST['appdata']
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if "1@asRsus$&sdnzh?sdbxjdAVShagdnhassffsdahjhdvjh" == api :
            if len(slug) > 2 and len(comment) > 10 and len(name) > 2 and len(email) > 2 and re.fullmatch(regex, email) :
                postname = Fresherjob.objects.get(slug = slug)
                jobcommments.objects.create(email=email,username=name,comments=comment,slug=postname, approvel=True)
                return HttpResponse(json.dumps({'request': "Comment Add succesfully"}),status = 200 , content_type="application/json")
            return HttpResponse(json.dumps({'request': "Write correct email or fill the form corret"}),status = 400 , content_type="application/json")
        return HttpResponse(json.dumps({'request': "unauthorized request"}),status = 400 , content_type="application/json")
    return HttpResponse(json.dumps({'request': "unauthorized request"}),status = 400 , content_type="application/json")

# all blog post method use 
def cmtToDictionary(cmts):
    output = {}
    output["sno"] = cmts.sno
    output["username"] = cmts.username
    output["post_time"] = cmts.post_time.strftime("%m/%d/%Y, %H:%M:%S")
    output["comments"] = cmts.comments
    output["approvel"] = cmts.approvel
    return output

@csrf_exempt
def showcomments(request):
    if request.method == "POST" and request.is_ajax:
        slug = request.POST['slug']
        api = request.POST['appdata']
        if "1@asRsus$&sdnzh?sdbxjdAVShagdnhassffsdahjhdvjh" == api :
            cmtpost = jobcommments.objects.filter(slug = Fresherjob.objects.get(slug = slug)).order_by('post_time').reverse() 
            temps = []
            for i in range(len(cmtpost)):
                temps.append(cmtToDictionary(cmtpost[i]))
            post = temps
            return HttpResponse(json.dumps({'request': post}),status = 200 , content_type="application/json")
        return HttpResponse(json.dumps({'request': "unauthorized request"}),status = 400 , content_type="application/json")
    return HttpResponse(json.dumps({'request': "unauthorized request"}),status = 400 , content_type="application/json")

def deletepost(request,ids):
    if request.user.is_authenticated:
        if request.method == "GET" and request.is_ajax:
            try:
                cmtsdata = jobcommments.objects.get(sno = ids)
                valuetoredirects = cmtsdata
                cmtsdata.delete()
                postname = Fresherjob.objects.get(title = valuetoredirects.slug)
                return HttpResponseRedirect(f"/{postname.slug}/#loadcmtbtnhai")
            except:
                return HttpResponse(json.dumps({'request': "unauthorized request"}),status = 400 , content_type="application/json")
        return HttpResponse(json.dumps({'request': "unauthorized request"}),status = 400 , content_type="application/json")
    else:
        return HttpResponseRedirect('/login/')
