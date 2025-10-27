from django.db import models

# Create your models here.

class Kichekesho(models.Model):
    """
    Model representing a Kichekesho (joke) entry.
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
  
class Picha(models.Model):
    """
    Model representing a Picha (image) entry.
    """
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='picha/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Hadithi(models.Model):
    """
    Model representing a Hadithi (story) entry.
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    """
    Model representing a contact message sent by a user.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} <{self.email}>" 
