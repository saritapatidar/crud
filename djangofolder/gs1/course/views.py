from django.shortcuts import render

# Create your views here.
def homes(request):
    return render(request,'core/init.html')