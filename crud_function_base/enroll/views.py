from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from .forms import StudentRegistration
from .models import user
# from django.views import View
# Create your views here.
def add_show(request):
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            reg=user(name=nm,email=em,password=pw)
            reg.save()
            fm=StudentRegistration()

    else:
        fm=StudentRegistration()
    stud=user.objects.all()
    return render(request,'enroll/addandshow.html',{'form':fm,'stu':stud})
def update_data(request,id):

    if request.method=='POST':
        pi=user.objects.get(pk=id)
        
        fm=StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=user.objects.get(pk=id)
        fm=StudentRegistration(instance=pi)
    return render(request,'enroll/updatestudent.html',{'form':fm})

def delete_data(request,id):
    if request.method=='POST':
        pi=user.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
    
# def update_data(request, id):
#     pi = user.objects.get(pk=id)  # Get the user instance once
#     if request.method == 'POST':
#         fm = StudentRegistration(request.POST, instance=pi)
#         if fm.is_valid():
#             fm.save()
#     else:
#         fm = StudentRegistration(instance=pi)  # Ensure fm is always defined
    
#     return render(request, 'enroll/updatestudent.html', {'form': fm})
