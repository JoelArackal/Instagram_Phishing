from django.shortcuts import render
from .models import UserData

# Create your views here.

def index(request,id=None):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password'] 
        print(username)
        print(password)
        user = UserData(username=username,password=password)
        user.save()
        return render(request,'account.html',{'user':username})

    return render(request,'index.html')