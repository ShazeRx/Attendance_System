from django.urls import path,include
from .views import ShowTeacherProfile


urlpatterns = [



    path('',ShowTeacherProfile.as_view(),name='profile'),


]