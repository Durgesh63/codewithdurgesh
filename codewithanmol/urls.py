
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "CodeWithanmol Admin"
admin.site.site_title = "CodeWithanmol Admin Panel"
admin.site.index_title = "Welcome to Codewithanmol Admin panel"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('fresher-job/', include('fresherjob.urls')),
]


handler404 = 'blog.views.error_404_view'
handler500 = 'blog.views.error_500_view'