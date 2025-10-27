from django.shortcuts import render
from .models import Kichekesho



# Create your views here.

def home(request):
    """ Render the home page of the Vichekesho application. """
    vichekesho = Kichekesho.objects.order_by('-created_at') 
    
  
    return render(request, 'vichekesho_app/home.html', {'vichekesho': vichekesho})

def about(request):
    """
    Render the about page of the Vichekesho application.
    """
    return render(request, 'vichekesho_app/about.html')

def contact(request):
    """
    Render the contact page of the Vichekesho application.
    """
    return render(request, 'vichekesho_app/contact.html')

def hadithi(request):
    """
    Render the hadithi page of the Vichekesho application.
    """
    return render(request, 'vichekesho_app/hadithi.html')

def picha(request):
    """
    Render the picha page of the Vichekesho application.
    """
    return render(request, 'vichekesho_app/picha.html')

def soma_kichekesho(request, kichekesho_id):
    """ Render a specific Kichekesho (joke) based on its ID. """
     
    kichekesho = Kichekesho.objects.get(id=kichekesho_id)
    vichekesho = Kichekesho.objects.order_by('-created_at')[:10]  # Latest 10 jokes
    return render(request, 'vichekesho_app/soma_kichekesho.html', {'kichekesho': kichekesho, 'vichekesho': vichekesho})