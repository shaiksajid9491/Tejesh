from django.conf import settings
from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import EmployeeForm, UserForm
from .models import Employee


# Create your views here.


def home(request):
    return render(request,"home.html")


def town(request):
    return HttpResponse("<h1>home town</h1>")


def table(request):
    emp = Employee.objects.all()
    return render(request, "table.html", {"record": emp})


def user_table(request):
    user = User.objects.all().values("username", "password", "first_name", "last_name")
    print(user)
    return render(request, "user.html", {"data": user})

def create(request):
    if request.method == 'POST':
        print(request.POST)
        form = EmployeeForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('/table/')
    else:
            form = EmployeeForm()
    return render(request,'create.html',{'form':form})


def edit(request, id):
    emp_data = Employee.objects.get(id=id)
    form = EmployeeForm(instance=emp_data)
    return render(request, "update.html", {'form': form, 'id': id})


def update(request, id):
    emp_data = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance=emp_data)
    if form.is_valid():
        form.save()
        return redirect('/table/')
    return render(request, "update.html", {'form': form,'id': id})


def delete(request, id):
    emp = Employee.objects.get(id=id)
    emp.delete()
    return redirect('/table/')


def registration(request):

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = request.POST.get("username")
            email = request.POST.get("email")
            password = request.POST.get("password")
            confirmpassword = request.POST.get("confirmpassword")
            if password == confirmpassword:
                User.objects.create_user(username=name, email=email, password=password)
                send_mail('Thank you '+name+' for registration',
                          'Here is your login Below \nhttp://127.0.0.1:9000/login/',
                          settings.EMAIL_HOST_USER,
                          [email]
                          )
                return redirect("/login/")
    else:
        form = UserForm()

    return render(request,"userregister.html",{"form":form})



def login(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('password')
        user = authenticate(username=uname, password=pwd)
        print(user)
        if user:
            return redirect('/table/')
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('/login/')
