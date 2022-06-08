from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth import authenticate
from .models import User
from django.contrib.auth.hashers import make_password
# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return render(request, 'landing.html')

def dashboard(request):
    if request.user.user_type=='DOCTOR':
        user_type = True
    else:
       user_type = False
    return render(request, 'dashboard.html', {user_type: user_type})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            
            return redirect('/dashboard')
        else:
            messages.warning(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'landing.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        role = request.POST['role']
        address = request.POST['address']
        fileobj = request.FILES
        print("profile pic is ",fileobj['profile_pic'])
        profile_pic = fileobj['profile_pic']
        # profile_pic = request.POST['profile_pic']
        if password1==password2:
            if User.objects.filter(username=username).exists == False:
                messages.info(request, 'Username Taken')
                return redirect(register)
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name, user_type=role, address=address, profile_pic=profile_pic)
                user.save()
        return redirect('/login')

    else:
        return render(request, 'landing.html')

def logout(request):
    auth.logout(request)
    return redirect('/')