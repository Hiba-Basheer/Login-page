from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.views.decorators.http import require_POST



@never_cache
def home(request):
    if request.user.is_authenticated:
        return render(request,'home.html')
    else:
        return redirect('login')

    
@never_cache
def SignupPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method=='POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        
        if pass1!=pass2:
            return HttpResponse("Your password and coform password are not matching")
        else:

           my_user=User.objects.create_user(username=uname,email=email,password=pass1)
           my_user.save()
        
           return redirect('login')
        
    return render (request,'signup.html')

@never_cache
def LoginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password is incorrect!!!")

    return render(request, 'login.html')

@never_cache
def LogoutPage(request):
    logout(request)
    return redirect('login')

# View for logging out
# Ensures logout can only be triggered by a POST request
# @require_POST
# def logout_user(request):
#     auth_logout(request)
#     return redirect('login')