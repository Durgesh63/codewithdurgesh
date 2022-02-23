from turtle import title
from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth import authenticate,login as auth_login,logout
from .forms import Login_form
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Blogs , Contact
from fresherjob.models import Fresherjob,jovvacancies
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
import re
import requests
# Create your views here.

"""
A utility function to convert object of type job to a Python Dictionary
"""
# all blog post method use 
def BlogToDictionary(Blog):
    output = {}
    output["id"] = Blog.id
    output["title"] = Blog.title
    output["date"] = Blog.date.strftime("%m/%d/%Y, %H:%M:%S")
    output["slug"] = Blog.slug
    output["description"] = Blog.description
    output["image"] = Blog.image
    output["meta_title"] = Blog.meta_title
    output["meta_short_description"] = Blog.meta_short_description    
    output["meta_tags"] = Blog.meta_tags
    return output

# all jobs post method use 
def JobsToDictionary(job):
    output = {}
    output["id"] = job.id
    output["title"] = job.title
    output["date"] = job.date.strftime("%m/%d/%Y, %H:%M:%S")
    output["slug"] = job.slug
    output["description"] = job.description
    output["image"] = job.image
    output["application_link"] = job.application_link
    output["company"] = job.company
    output["job_experience"] = job.job_experience
    output["salary"] = job.salary
    output["passing_year"] = job.passing_year
    output["location"] = job.location
    output["degree"] = job.degree
    output["role_name"] = job.role_name
    output["meta_title"] = job.meta_title
    output["meta_short_description"] = job.meta_short_description
    output["meta_tags"] = job.meta_tags
    return output

@csrf_exempt
def getallpostdata(request):
    if request.method == "POST" and request.is_ajax:
        try:
            post = request.POST['model']
            try:
                num = int(request.POST['total_output'])
            except:
                pass 
            publish = str(request.POST['publish'])
            api = request.POST['api']
            api_key = '1@asRsus$&sdnzh?sdbxjdAVShagdnhassff'
            if api_key == api:
                if post == "blogs":
                    model_name=Blogs
                elif post == "fresherjob":
                    model_name = Fresherjob
                else:
                    pass
                try:
                    posts_data = model_name.objects.filter(publish=publish).order_by('date').reverse()[:num]
                except:
                    posts_data = model_name.objects.filter(publish=publish).order_by('date').reverse() 
                temps = []
                for i in range(len(posts_data)):
                    if post == "blogs":
                        temps.append(BlogToDictionary(posts_data[i])) # Converting `QuerySet` to a Python Dictionary
                    elif post == "fresherjob":
                        temps.append(JobsToDictionary(posts_data[i])) # Converting `QuerySet` to a Python Dictionary
                    else:
                        pass
                post = temps
                return HttpResponse(json.dumps({'request':post}), content_type="application/json")
            return HttpResponse(json.dumps({'request':"request error" }),status = 400 , content_type="application/json")
        except:
            return HttpResponse(json.dumps({'request':"request error" }),status = 500 , content_type="application/json")
    return HttpResponse(json.dumps({'request': "request error"}),status = 400 , content_type="application/json")

def homepage(request):
    return render(request,'blog/homepage.html',{'current_path': request.build_absolute_uri()})


def blog(request):
    return render(request,'blog/blog.html',{'current_path': request.build_absolute_uri()})

def content(request,slug):
    content_data = Blogs.objects.get(slug=slug , publish="publish")
    return render(request,'blog/contents.html',{"data":content_data ,'current_path': request.build_absolute_uri()})

def about(request):
    return render(request,'blog/about.html',{'current_path': request.build_absolute_uri()})


def contectus(request):
    if request.method == "POST":
        email = request.POST['email']
        name = request.POST['name']
        query = request.POST['contact_query']
        message = request.POST['message']
        Reference_link = request.POST['reference_link']
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(regex, email) and all(x.isalpha() or x.isspace() for x in name) :
            if len(query) > 0 and len(name) > 0 and len(email) > 5 and len(message) > 5:
                if Contact.objects.filter(email=email).exists():
                    messages.error(request,'Already fill the form please wait for the Respose & Please Check Your Email ')
                else:
                    Contact.objects.create(email=email,name=name,query=query,message=message,Reference_link=Reference_link)
                    messages.success(request,f"Succefully contact form save. Wait for Response.")
                    return HttpResponseRedirect('/contect-us/')
            else:
                messages.error(request,f"Please enter a full informations .Change a few things up and try submitting again.")
        else:
            messages.error(request,f"Please enter a correct '{email} or {name} ' .Note that email and Full Name fields may be case-sensitive and Change a few things up and try submitting again.") 
    return render(request,'blog/contectus.html',{'current_path': request.build_absolute_uri()})


def editor(request,slug):
    if request.user.is_authenticated:
        content_data = Blogs.objects.get(slug=slug)
        return render(request,'blog/editblogpost.html',{"data":content_data ,'current_path': request.build_absolute_uri()})
    else:
        return HttpResponseRedirect('/login/')

def term_conditions(request):
    return render(request,'blog/termandconditions.html',{'current_path': request.build_absolute_uri()})

# login function
def login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form=Login_form(request=request, data=request.POST)
            usrname = request.POST['username']
            usrpass = request.POST['password']
            user = authenticate(username=usrname, password=usrpass) #form authention
            if user is not None:
                if user.is_active:
                    auth_login(request,user)
                    messages.success(request,f"Hello  ' {usrname} ' login succefully!!")
                    return HttpResponseRedirect('/dashboard/')   
            elif not User.objects.filter(username = usrname).exists():
                messages.error(request,f"Please enter a correct ' {usrname} ' and password. Note that both fields may be case-sensitive.")
                return HttpResponseRedirect('/login/') 
            else:
                messages.error(request,f"Please enter a correct ' {usrname} ' and password. Note that both fields may be case-sensitive.")
                return HttpResponseRedirect('/login/') 
        else:
            form=Login_form()
        return render(request,'blog/login.html',{'form':form})

    else:
        return HttpResponseRedirect('/')

#logout function
def log_out(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,f"Thankyou!! Logout succefully!!")
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/login/')


@csrf_exempt
def editpostdata(request):
    if request.user.is_authenticated:
        if request.method == "POST" and request.is_ajax:
            try:
                print("button click")
                slug = request.POST['slug']
                model_names = request.POST['model_name']
                title = request.POST['title']
                publishs = request.POST['publish']
                description = request.POST['description']
                thumbnail = request.POST['thumbnail']
                seo_title = request.POST['seo_title']
                seo_desc = request.POST['seo_desce']
                seo_tag = request.POST['seo_tag']
                api = request.POST['api']
                api_key = '1@asRsus$&sdnzh?sdbxjdAVShagdnhassff'
                if publishs== "draft":
                    publish = "Draft"
                elif publishs== "publish":
                    publish = "publish"
                if api_key == api and len(title) > 0 and len(slug)>0:
                    if model_names == "Blog":
                        model_name = Blogs
                        update_post = model_name.objects.get(slug=slug)
                        update_post.publish = publish
                        update_post.title = title
                        update_post.description = description
                        update_post.image = thumbnail
                        update_post.meta_title = seo_title
                        update_post.meta_short_description = seo_desc
                        update_post.meta_tags = seo_tag
                        update_post.save()
                        return HttpResponse(json.dumps({'request': "Data will Save Succefully !!"}), status = 200 , content_type="application/json")
                    elif model_names == "Fresher":
                        model_name = Fresherjob
                        update_post = model_name.objects.get(slug=slug)
                        update_post.publish = publish
                        update_post.title = title
                        update_post.description = description
                        update_post.image = thumbnail
                        update_post.meta_title = seo_title
                        update_post.meta_short_description = seo_desc
                        update_post.meta_tags = seo_tag
                        update_post.company = request.POST['company_name']
                        update_post.job_experience = request.POST['job_experience']
                        update_post.salary = request.POST['salary']
                        update_post.passing_year = request.POST['passing_year']
                        update_post.location = request.POST['location']
                        update_post.degree = request.POST['degree']
                        update_post.role_name = request.POST['role_name']
                        update_post.application_link = request.POST['application_link']
                        update_post.save()
                        print(seo_tag ,model_name ,title,slug ,description ,thumbnail ,seo_title ,seo_desc , publish)
                        return HttpResponse(json.dumps({'request':"Data will Save Succefully !!" }),status = 200 , content_type="application/json")
                    else:
                        pass
                else:
                    return HttpResponse(json.dumps({'request':"request error" }),status = 400 , content_type="application/json")
            except:
                print("button click 1")
                return HttpResponse(json.dumps({'request':"request error" }),status = 500 , content_type="application/json")
        return HttpResponse(json.dumps({'request': "request error"}),status = 400 , content_type="application/json")
    else:
        return HttpResponseRedirect('/login/')


def error_404_view(request,exception):
    return render(request,'blog/404.html',{'current_path': request.build_absolute_uri()})


def error_500_view(request):
    return render(request,'blog/500.html',{'current_path': request.build_absolute_uri()})


def dashboard(request):
    user = request.user
    return render(request,'blog/dashboard.html',{"username":user,'current_path': request.build_absolute_uri()})


def newblogpost(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            blog_title = request.POST['blog_title']
            if len(blog_title) > 0:
                Blogs.objects.create(title=blog_title)
                messages.success(request,f"Blog Save '{blog_title}' succefully!!")
                return HttpResponseRedirect('/view-blog-post/')
        return render(request,'blog/newpost.html',{"blog":True,'current_path': request.build_absolute_uri()})
    else:
        return HttpResponseRedirect('/login/')

def newfresherpost(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fresher_title = request.POST['fresher_title']
            if len(fresher_title) > 0:
                Fresherjob.objects.create(title=fresher_title)
                messages.success(request,f"Blog Save '{fresher_title}' succefully!!")
                return HttpResponseRedirect('/view-fresher-post/')
        return render(request,'blog/newpost.html',{"blog":False,'current_path': request.build_absolute_uri()})
    else:
        return HttpResponseRedirect('/login/')

def seeblogpost(request):
    if request.user.is_authenticated:
        blog = Blogs.objects.all().order_by('date').reverse()
        return render(request,'blog/viewpost.html',{"blog":"blog","data":blog,'current_path': request.build_absolute_uri()})
    else:
        return HttpResponseRedirect('/login/')

def seefresherpost(request):
    if request.user.is_authenticated:
        fresher = Fresherjob.objects.all().order_by('date').reverse()
        return render(request,'blog/viewpost.html',{"blog":"fresher","data":fresher,'current_path': request.build_absolute_uri()})
    else:
        return HttpResponseRedirect('/login/')

def seecontentpost(request):
    if request.user.is_authenticated:
        contacts = Contact.objects.all().order_by('date').reverse()
        return render(request,'blog/viewpost.html',{"blog":"contact","data":contacts,'current_path': request.build_absolute_uri()})
    else:
        return HttpResponseRedirect('/login/')

def seejobvacanciespost(request):
    if request.user.is_authenticated:
        vacancies = jovvacancies.objects.all().order_by('date').reverse()
        return render(request,'blog/viewpost.html',{"blog":"jobvacancies","data":vacancies,'current_path': request.build_absolute_uri()})
    else:
        return HttpResponseRedirect('/login/')

def sendtelegrammsg(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            img_link = request.POST['imagefile']
            text = request.POST['text']
            if img_link :
                send_msg = f'https://api.telegram.org/bot5014601093:AAENCbjtNqHPCU2j0PZOy7YTrutZnssEcsQ/sendPhoto?chat_id=@Fresher_job&photo={img_link}&caption={text}'
                r= requests.get(send_msg)
                if r.status_code == 200:
                    messages.success(request,f"Message send Succefully!!")
                return HttpResponseRedirect('/send-telegram-msg/')   
            else:
                send_msg = f'https://api.telegram.org/bot5014601093:AAENCbjtNqHPCU2j0PZOy7YTrutZnssEcsQ/sendMessage?chat_id=@Fresher_job&text={text}'
                r =requests.get(send_msg)
                if r.status_code == 200:
                    messages.success(request,f"Message send Succefully!!")
                return HttpResponseRedirect('/send-telegram-msg/')   
        return render(request,'blog/viewpost.html',{"blog":"telegram",'current_path': request.build_absolute_uri()})
    else:
        return HttpResponseRedirect('/login/')


def deletepost(request,slug,model):
    if request.user.is_authenticated:
        try:
            if model == "blog":
                post_name = [ ]
                post_to_delete=Blogs.objects.get(slug=slug)
                post_name.append(post_to_delete.title)
                post_to_delete.delete()
                messages.success(request,f"Blog - {post_name}  Deleted Successfully")
                return HttpResponseRedirect('/view-blog-post/')
            elif model == "fresher":
                post_name = [ ]
                post_to_delete=Fresherjob.objects.get(slug=slug)
                post_name.append(post_to_delete.title)
                post_to_delete.delete()
                messages.success(request,f"Fresherjob - {post_name}  Deleted Successfully")
                return HttpResponseRedirect('/view-fresher-post/')
            elif model == "contact":
                post_name = [ ]
                post_to_delete=Contact.objects.get(id=slug)
                post_name.append(post_to_delete.email)
                post_to_delete.delete()
                messages.success(request,f"Fresherjob - {post_name}  Deleted Successfully")
                return HttpResponseRedirect('/view-contants-post/')
            elif model == "jobvacancies":
                post_name = [ ]
                post_to_delete=jovvacancies.objects.get(id=slug)
                post_name.append(post_to_delete.email)
                post_to_delete.delete()
                messages.success(request,f"Fresherjob - {post_name}  Deleted Successfully")
                return HttpResponseRedirect('/view-job-vacancies-post/')
            else:
                messages.error(request,f"Post  not found. Please Try again ")
                return HttpResponseRedirect('/dashboard/')
        except:
            messages.error(request,f"Post  not found. Please Try again ")
            return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')
