
from django.contrib import admin
from django.urls import path, include 

admin.site.site_header = "Macks Admin"
admin.site.site_title = "Macks Admin Portal"
admin.site.index_title = "Welcome to Macks Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls'))
    
]
