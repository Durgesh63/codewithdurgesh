from django.contrib import admin

# Register your models here.
from .models import Blogs , Contact

# Register your models here.
@admin.register(Blogs)
class Blogsadmin(admin.ModelAdmin):
    class Media:
        list_display = ['id','title']

@admin.register(Contact)
class Contactadmin(admin.ModelAdmin):
    class Media:
        list_display = ['email']