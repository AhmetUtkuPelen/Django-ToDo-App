from django.urls import path
from .views import*
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static





urlpatterns = [
    path('',index,name="index"),
    path('about/',about,name="about"),
    path('create/',create,name="create"),
    path('delete/<Todos_id>',delete,name="delete"),
    path('finished/<Todos_id>',finished,name="finished"),
    path('notfinished/<Todos_id>',notfinished,name="notfinished"),
    path('update/<Todos_id>',update,name="update"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)





admin.site.site_header = "AUP TECH"
admin.site.site_title = "AUP TECH"