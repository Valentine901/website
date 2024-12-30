from django.contrib import admin
from .models import Me, Port, Service, Test, Message
# Register your models here.
admin.site.register(Me)
admin.site.register(Port)
admin.site.register(Service)
admin.site.register(Test)
admin.site.register(Message)
