from django.urls import path
from app import views

urlpatterns=[
    path("", views.index, name="index"),
    path("index", views.index, name="index"),
    path("home", views.home, name="home"),
    path("login", views.ulogin, name="login"),
    path('logout', views.logoutuser , name="logoutuser"),
    path("recipe", views.recipe, name="recipe"),

]