from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello world! this is my show.")


def signup(request):
    return render(request, "authentication/signup.html")


def login(request):
    return render(request, "authentication/login.html")


# def logout(request):
#     return render(request, "authentication/logout.html")

def logout(request):
    pass