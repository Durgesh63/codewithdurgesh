from django.db import models
from autoslug import AutoSlugField

# Create your models here.

PUBLISH_CHOICES = (   
    ("Draft", "Draft"),   
    ("hold", "hold"),   
    ("publish", "publish"),     
)

class Fresherjob(models.Model):
    publish = models.CharField(max_length = 40,choices = PUBLISH_CHOICES,default="Draft",verbose_name ='Post Details' )

    title = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now = True,verbose_name = 'Post Date')
    slug = AutoSlugField(populate_from='title',unique_with=['id'],null=True,blank=True)
    description = models.TextField(null=True,blank=True,verbose_name = 'Blog Description')
    image = models.URLField(max_length =1000,null=True,default="https://res.cloudinary.com/anmoldev/image/upload/v1645635518/Screenshot_from_2022-02-23_22-25-18_eoq6r9.png",blank=True,verbose_name = 'Image link')

    application_link = models.URLField(max_length =1000,null=True,blank=True,verbose_name = 'Form link')

    company = models.CharField(max_length=500,null=True,blank=True,verbose_name = 'Company Name')
    job_experience = models.CharField(max_length=500,null=True,blank=True,verbose_name = 'Job Experience')
    salary = models.CharField(max_length=500,null=True,blank=True,verbose_name = 'Salary')
    passing_year = models.CharField(max_length=500,null=True,blank=True,verbose_name = 'Passing Year')
    location = models.CharField(max_length=500,null=True,blank=True,verbose_name = 'Location')
    degree = models.CharField(max_length=500,null=True,blank=True,verbose_name = 'Degree')
    role_name = models.CharField(max_length=500,null=True,blank=True,verbose_name = 'Role Name')


    meta_title = models.CharField(max_length=500,verbose_name = 'Meta Title',null=True,blank=True)
    meta_short_description = models.CharField(max_length=500,verbose_name = 'Short Description',null=True,blank=True)
    meta_tags = models.CharField(max_length=300,verbose_name = 'Meta Tags',null=True,blank=True)
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Fresherjob'


class jovvacancies(models.Model):
    email = models.EmailField(max_length=100,verbose_name = 'Email Address')
    date = models.DateTimeField(auto_now = True,verbose_name = 'Post Date')
    company = models.CharField(max_length=500,verbose_name = 'Company Name')
    location = models.CharField(max_length=500,verbose_name = 'Location')
    role_name = models.CharField(max_length=500,verbose_name = 'Role Name')
    job_experience = models.CharField(max_length=500,verbose_name = 'Job Experience')
    qualifications = models.CharField(max_length=500,verbose_name = 'Qualifications')
    application_link = models.URLField(max_length =500 ,null=True,blank=True, verbose_name = 'Reference link')
    
    def __str__(self):
        return self.company + ' ' + self.role_name + ' ' + self.qualifications
    class Meta:
        verbose_name = 'Vacancie'