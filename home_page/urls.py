from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
     path('', views.home, name="home"),
    path('blog/', views.blog, name="blog"),
    path('homeMessageSucess/',views.homeMessageSucess,name="homeMessageSucess"),
    path('CommingSoon/', views.CommingSoon, name="CommingSoon"),

]


