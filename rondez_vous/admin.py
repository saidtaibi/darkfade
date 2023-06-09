from django.contrib import admin
from .models import Coupe, Category, ContactMessage, Appointment

# Register your models here.
admin.site.register(Coupe)
admin.site.register(Category)
admin.site.register(ContactMessage)
admin.site.register(Appointment)

