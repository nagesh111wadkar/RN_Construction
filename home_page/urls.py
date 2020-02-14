from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    # path('', views.view1),
    path('', views.home, name="home"),
    path('blog/', views.blog, name="blog"),
    # path('contactform/contact.html', views.contact, name="contact"),
    # path('conformMessage/', views.conformMessage, name="conformMessage"),


]


