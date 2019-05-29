
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.contrib.auth import authenticate, login
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',auth_views.LoginView.as_view(),name='login'),
    path('login/',auth_views.LogoutView.as_view(),name='logout')

]

