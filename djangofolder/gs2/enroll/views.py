from django.shortcuts import render
from enroll.models import Student
# Create your views here.
def studinfo(request):
    stud=Student.objects.all()
    return render(request,'enroll/student.html',{'stu':stud})