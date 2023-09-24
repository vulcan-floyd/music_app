from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from django.views import View


# Create your views here.
class LogIn(View):
    def get(self, request):
        return render(request, 'signin.html')
    
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username,
                                 password=password)
        if user:
            auth.login(request, user)
            return render(request, 'index.html')
        else:
            messages.info(request, 'Account Not Found')
            return redirect('login')

class SignUp(View):
    def get(self, request):
        return render(request, 'signup.html')
    
    def post(self, request):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password']
        
        if password != password2:
            messages.info(request, 'Password does not match')
            return redirect('signup')
        else:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'email already exists')
                return redirect('signin')
            else:
                user = User.objects.create_user(username=username,
                                                email=email,
                                                password=password)
                user.save()
                user_login = auth.authenticate(username=username,
                                         password=password)
                auth.login(request, user_login)
                return render(request, 'index.html')

# class LogOut(View):
#     @login_required
def Logout(request):
    auth.logout(request)
    return redirect('login')
            