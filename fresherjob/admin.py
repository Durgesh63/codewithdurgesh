from django.contrib import admin
from .models import Fresherjob,jovvacancies

# Register your models here.
@admin.register(Fresherjob)
class Fresherjobadmin(admin.ModelAdmin):
    class Media:
        list_display = ['id','title']

@admin.register(jovvacancies)
class Jovvacanciesadmin(admin.ModelAdmin):
    class Media:
        list_display = ['id','email']