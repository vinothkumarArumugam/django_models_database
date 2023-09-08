from django.contrib import admin
from dbapp.models import employee     -----# importing class(model) from models.py file

# Register your models here.
admin.site.register(employee)    ----#registering our models in admin.py file
