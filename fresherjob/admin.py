from django.contrib import admin
from .models import Fresherjob,jovvacancies,jobcommments

# Register your models here.
@admin.register(Fresherjob)
class Fresherjobadmin(admin.ModelAdmin):
    class Media:
        list_display = ['id','title']

@admin.register(jovvacancies)
class Jovvacanciesadmin(admin.ModelAdmin):
    class Media:
        list_display = ['id','email']

@admin.register(jobcommments)
class Jovcommentsadmin(admin.ModelAdmin):
    class Media:
        list_display = ['sno','email','username']