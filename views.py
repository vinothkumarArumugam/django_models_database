from django.shortcuts import render
from app1.models import student #getting information from models
def student_details(request):
    student_data=student.objects.all()
    student_dict={"student_details":student_data}
    return render(request,'app1/student.html',context=student_dict)
