from django.urls import path 
from . import views

urlpatterns = [
    path('fresher-job/',views.fresherjob, name ="fresherjob"),
    path('fresher-job/content/',views.freshercontent, name ="fresherjobcontent"),
    path('fresher-job/post-job-vacancies/',views.postjob, name ="postjob"),
    path('<slug:slug>/',views.contents, name ="contents"),
    path('fresher-job/content/edit/<slug:slug>/',views.editor, name ="editor"),
]