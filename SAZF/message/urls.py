from django.urls import path
from .views import ShowMessages


urlpatterns = [



    path('',ShowMessages.as_view(),name='messages'),



]