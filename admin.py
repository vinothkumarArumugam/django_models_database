from django.contrib import admin
from app1.models import student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=["student_name",'student_fees','student_mark']
admin.site.register(student,StudentAdmin)
