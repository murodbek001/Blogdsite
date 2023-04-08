from django.urls import path
from .views import index,about,services,contact

urlpatterns = [
     path('',index, name="index"),
     path('about/', about,name="about"),
     path('services/', services,name="services"),
     path('contact/', contact,name="contact"),

]