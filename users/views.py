from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request):
    """
    Render the home page for the users app.
    """
    return HttpResponse("Welcome to the Users Home Page")