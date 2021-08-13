from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('question/',views.poseQuestion,name='poseQuestion'),
    path('about/', views.about, name='about'),
    path('share/', views.share, name='share'),
]