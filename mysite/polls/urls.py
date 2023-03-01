from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('<int:question_id>/', views.detail.as_view(), name='detail'),
    path('stam/', views.stam, name='stam'),
    path('<int:question_id>/vote', views.Vote.as_view(),name='vote'),
    path('newq/', views.NewQuestion.as_view(),name="newquestion"),
    path('newc/', views.NewChoice.as_view(),name='newchoice'),
]