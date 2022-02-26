from django.db import models
from autoslug import AutoSlugField
from datetime import datetime

# Create your models here.

PUBLISH_CHOICES = (   
    ("Draft", "Draft"),   
    ("hold", "hold"),   
    ("publish", "publish"),     
)

class Blogs(models.Model):
    publish = models.CharField(max_length = 40,choices = PUBLISH_CHOICES,default="Draft",verbose_name ='Post Details' )

    title = models.CharField(max_length=500)
    date = models.DateTimeField(default=datetime.now ,verbose_name = 'Post Date')
    updatedate = models.DateTimeField(auto_now = True,verbose_name = 'Update Date')
    slug = AutoSlugField(populate_from='title',unique_with=['id'],null=True,blank=True)
    description = models.TextField(null=True,blank=True,verbose_name = 'Blog Description')
    image = models.URLField(max_length =1000,null=True,default="https://res.cloudinary.com/anmoldev/image/upload/v1645629950/Screenshot_from_2022-02-23_20-53-28_aynez4.png",blank=True,verbose_name = 'Image link')

    meta_title = models.CharField(max_length=500,verbose_name = 'Meta Title',null=True,blank=True)
    meta_short_description = models.CharField(max_length=500,verbose_name = 'Short Description',null=True,blank=True)
    meta_tags = models.CharField(max_length=300,verbose_name = 'Meta Tags',null=True,blank=True)
    
    def __str__(self):
        return 'BLOG POST - ' + self.title
    class Meta:
        verbose_name = 'Blog'

class Contact(models.Model):
    email = models.EmailField(max_length=100 ,unique = True, error_messages = {"unique":"The Email Field you entered is not unique."})
    date = models.DateTimeField(auto_now = True,verbose_name = 'Post Date')
    name = models.CharField(max_length=100,verbose_name = 'Full Name')
    query = models.CharField(max_length=150,verbose_name = 'Query',null=True,blank=True)
    message = models.TextField(verbose_name = 'Message')
    Reference_link = models.URLField(max_length =500,null=True,blank=True,verbose_name = 'Reference link')

    
    def __str__(self):
        return self.email + ' ' + self.name
    class Meta:
        verbose_name = 'Contact'