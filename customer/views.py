from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.views import LoginView, LogoutView


from core.models import Myuser
from core.views import Home



# Create your views here.
from .models import Customer
from .vlidator import validat_phone


class SingUp(View):

    def post(self, request):
        username = request.POST['username']
        first_name = request.POST['name']
        password = request.POST['password']

        if validat_phone(username) == True:
            new_user = Myuser.objects.create_user(username=username, first_name=first_name, password=password,
                                                  phone=username)
            customer = Customer.objects.create(user=new_user)
            return HttpResponse(f'register {new_user.first_name}')
        else:
            return HttpResponse('phone is not validate')

    def get(self, request):
        return render(request, 'sing_up.html')


class LoginView(LoginView):

    template_name = 'login.html'


from django.contrib.auth import logout


def logout_view(request):
    logout(request)
    return redirect('home')