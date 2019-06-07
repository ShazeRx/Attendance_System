from django.urls import path, include
from .views import show_dashboard


urlpatterns = [
    path('',show_dashboard ),

]