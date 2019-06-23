from django.urls import path
from .views import ShowMessages,SendMessage,MessageDetail
from django.conf.urls.  static import static



urlpatterns = [



    path('',ShowMessages.as_view(),name='messages'),
    path('new_message/',SendMessage.as_view(),name='new_message'),
    path('<int:pk>/',MessageDetail.as_view(),name='message_detail'),



]