from django.urls import path,include
from .views import ShowTeacherProfile,EditTeacherProfile


urlpatterns = [



    path('',ShowTeacherProfile.as_view(),name='profile'),
    path('edit',EditTeacherProfile.as_view(),name='edit-profile')


]