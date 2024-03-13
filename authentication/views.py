from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    return render(request, "authentication/index.html")

def signup(request):
    if request.method == "POST":
        employeeid = request.POST['employeeid']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(employeeid, email, pass1)
        myuser.save()

        messages.success(request, "Your account has been successfully created.")

        return redirect('signin')        
    return render(request, "authentication/signup.html")

def signin(request):
    if request.method == "POST":
        employeeid = request.POST['employeeid']
        pass1 = request.POST['pass1']

        user = authenticate(username = employeeid, password = pass1)

        if user is not None:
            login(request, user)
            return render(request, "authentication/index.html", {'employeeid' : employeeid})

        else:
            messages.error(request, "Invalid credentials")
            return redirect('home')

    return render(request, "authentication/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('home')
    
