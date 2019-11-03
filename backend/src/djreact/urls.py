from django.contrib import admin
from django.urls import path,include
import rest_framework 

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('api/', include("articles.api.urls")) #this will take you to the api
]
