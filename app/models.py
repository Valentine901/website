from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Me(models.Model):
    STATUS = {
        'Available':'Available',
        'Unavaliable':'Unavaliable'
    }
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    city = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    date_birth = models.CharField(max_length=200)
    age = models.IntegerField()
    degree = models.CharField(max_length=200)
    body = models.TextField(default='')
    status = models.CharField(max_length=200, choices=STATUS)
    image = models.ImageField(upload_to='media', default='default')
    year = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.firstname

class Port(models.Model):
    app_image = models.ImageField(upload_to='media', default='default')
    card_image = models.ImageField(upload_to='media', default='default')
    web_image = models.ImageField(upload_to='media', default='default')
    link_tag = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.link_tag
    
class Service(models.Model):
    title = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name
    
class Test(models.Model):
    body = models.TextField( null=True)
    username = models.CharField(max_length=200, null=True)
    job = models.CharField(max_length=200, null=True)
    user_image = models.ImageField(upload_to='media', default='default', null=True, blank=True)
    def __str__(self):
        return self.username
    
class Message(models.Model):
    username = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    topic = models.CharField(max_length=200, null=True, blank=True)
    body = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.username