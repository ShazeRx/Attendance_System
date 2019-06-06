from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import show_notes
from .views import NoteDetail, NoteDelete,NoteUpdate

urlpatterns = [



    path('',show_notes,name='notes' ),
    path('<int:pk>',NoteDetail.as_view()),
    path('<int:pk>/delete',NoteDelete.as_view()),
    path('<int:pk>/update',NoteUpdate.as_view()),

]