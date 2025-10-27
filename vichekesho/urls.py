from django.contrib import admin
from django.urls import path, include
from vichekesho_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Make the 'about' page the default homepage
    path('', views.about, name='about-default'), 
    path('app/', include('vichekesho_app.urls')),
    path('users/', include('users.urls')),
]