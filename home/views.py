from django.shortcuts import render, HttpResponse

def index(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def jobs(request):
    return render(request,"jobs.html")