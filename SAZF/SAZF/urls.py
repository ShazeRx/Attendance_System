
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.contrib.auth import authenticate, login
from django.contrib.auth import views as auth_views
from django.conf.urls.  static import static
from django.conf import settings
from .views import pagelogout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',auth_views.LoginView.as_view(),name='login'),
    path('logout/',pagelogout,name='logout'),
    path('main/',include('main.urls') ),
    path('notes/',include('notes.urls') ),
    path('teacher/',include('teacher.urls') ),
    path('messages/',include('message.urls') ),
    path('',include('dashboard.urls') ),

]

