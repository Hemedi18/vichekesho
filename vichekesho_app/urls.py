from django.urls import path
from . import views

app_name = 'vichekesho_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('hadithi', views.hadithi, name='hadithi'),
    path('picha', views.picha, name='picha'),
    path('soma/<int:kichekesho_id>/', views.soma_kichekesho, name='soma_kichekesho'),
]
