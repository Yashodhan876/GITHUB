from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def frontpage(request):
    if request.user.is_authenticated:
        return redirect('userpage')
    return render(request, 'home/frontpage.html')

def register(request):
    return render(request, 'home/registration.html')

def contact(request):
    return render(request, 'home/contactus.html')

def about(request):
    return render(request, 'home/aboutus.html')

def handleSignup(request):
    if request.method == 'POST':
        # Get the post parameters
        username = request.POST['username']
        email = request.POST['email']
        phno = request.POST['phno']
        prnno = request.POST['prnno']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        #Check for errors
        if len(username)<10:
            messages.error(request,'Error. Username Should be atleast 10 characters.')
            return redirect('register')

        if not username.isalnum():
            messages.error(request,'Error. Username Should only contain letters and numbers.')
            return redirect('register')

        if (pass1!= pass2):
            messages.error(request,'Error. Password do not match.')
            return redirect('register')

        #Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.save()
        messages.success(request,"Your account has been successfully created")
        return redirect('register')

    else:
        return HttpResponse('<h1>404-Error</h1>')

def handleLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request,"SuccessFully Logged In")
            return redirect('userpage')
        else:
            return HttpResponse('<h1>Invalid Credentials. Please Try Again.</h1>')

    return HttpResponse("404- Not found")


def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('frontpage')

def handleadminLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None and user.is_superuser:
            login(request, user)
            messages.success(request,"SuccessFully Logged In")
            return redirect('AdmnUser')
        else:
            return HttpResponse('<h1>Invalid Credentials. Please Try Again.</h1>')

    return HttpResponse("404- Not found")


def handleadminLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('frontpage')