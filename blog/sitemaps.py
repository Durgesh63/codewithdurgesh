from django.contrib import sitemaps
from django.urls import reverse
from .models import Blogs
from fresherjob.models import Fresherjob



class Home(sitemaps.Sitemap):
    priority = 1.0
    changefreq = 'daily'

    def items(self):
        return ['homepage']

    def location(self, item):
        return reverse(item)

 
class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.8
    changefreq = 'daily'

    def items(self):
        return ['fresherjob','blog','fresherjobcontent','postjob','about','contectus','term_conditions']

    def location(self, item):
        return reverse(item)


class Blog(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return Blogs.objects.filter(publish='publish')

    def location(self,obj):
        return f'/blog/{obj.slug}/'
        
    def lastmod(self, obj):
        return obj.date

class Fresher(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return Fresherjob.objects.filter(publish='publish')

    def location(self,obj):
        return f'/fresher-job/content/{obj.slug}/'
        
    def lastmod(self, obj):
        return obj.date