from django.urls import path 
from . import views

urlpatterns = [
    path('',views.fresherjob, name ="fresherjob"),
    path('content/',views.freshercontent, name ="fresherjobcontent"),
    path('post-job-vacancies/',views.postjob, name ="postjob"),
    path('content/<slug:slug>/',views.contents, name ="contents"),
    path('content/edit/<slug:slug>/',views.editor, name ="editor"),
]