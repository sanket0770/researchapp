from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import boto3
from app.models import recipebook
import os
from app.s3_utils import S3Utils
from django.conf import settings
from project.settings import BUCKET, UPLOAD_FOLDER

# Create your views here.
def index(request):
    return render (request, "index.html")

def ulogin(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password= request.POST.get('password')
        print(username, password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')

def logoutuser(request):
    logout(request)
    return redirect("/index")

def home(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            k = recipebook.objects.all().values()
        return render (request, "home.html",{"k" : k})
    return redirect('login')

def recipe(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            name=request.POST.get('name')
            author=request.POST.get('author')
            ingredient=request.POST.get('ingredient')
            recipe=request.POST.get('recipe')
            f = request.FILES['imgInp']           
            if f.name != '':  # ensure that only upload to S3 if a file has been provided
                path = os.path.join(UPLOAD_FOLDER, f.name)
                with open(path, 'wb') as destination:
                    for chunk in f.chunks():
                        destination.write(chunk)

                S3Utils.upload_file('rbook-bucket', path, f.name) #forward bucket name, file path and file name to the upload_file

                if os.path.isfile(path) or os.path.islink(path):
                    os.remove(path)  # remove the file from the application (i.e. machine that hosts this application)
            obj_key=str(f)
            image = "https://rbook-bucket.s3.eu-west-2.amazonaws.com/"+obj_key #retrive the URL of uploaded obect
            r1 = recipebook(name=name, author=author, ingredient=ingredient, recipe=recipe, image=image)
            r1.save()                  
        return render (request, 'recipe.html')
    return redirect('login')

