from django.urls import path 
from . import views

from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap,Home,Blog,Fresher


sitemaps = {
    'home':Home,
    'static': StaticViewSitemap,
    'Blogs': Blog,
    'Fresherjobs': Fresher,
}


urlpatterns = [
    path('',views.homepage, name ="homepage"),
    path('blog/',views.blog, name ="blog"),
    path('blog/<slug:slug>/',views.content, name ="content"),
    path('about-us/',views.about, name ="about"),
    path('contect-us/',views.contectus, name ="contectus"),
    path('login/',views.login, name ="login"),
    path('logout/',views.log_out, name ="logout"),
    path('blog/edit/<slug:slug>/',views.editor, name ="editorblog"),
    path('term-and-conditions/',views.term_conditions, name ="term_conditions"),
    path('all-post-data/',views.getallpostdata, name ="getallpostdata"),
    path('data/',views.editpostdata, name ="editpostdata"),


    path('dashboard/',views.dashboard, name ="dashboard"),
    path('add-blog-post/',views.newblogpost, name ="newblogpost"),
    path('add-fresher-post/',views.newfresherpost, name ="newfresherpost"),
    path('view-blog-post/',views.seeblogpost, name ="seeblogpost"),
    path('view-fresher-post/',views.seefresherpost, name ="seefresherpost"),
    path('view-contants-post/',views.seecontentpost, name ="seecontentpost"),
    path('view-job-vacancies-post/',views.seejobvacanciespost, name ="seejobvacanciespost"),
    path('send-telegram-msg/',views.sendtelegrammsg, name ="sendtelegrammsg"),

    path('delete-post/<str:model>/<slug:slug>/',views.deletepost, name ="deletepost"),

    # sitemap 
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},name='django.contrib.sitemaps.views.sitemap'),  
]