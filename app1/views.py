from django.shortcuts import render, redirect
from app1.models import Employees
from .forms import EmployeeForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm


# Create your views here.

def home(request):
    return render (request, 'home.html')

def about(request):
    return render (request, 'about.html')

def contact(request):
    return render (request, 'contact.html')

def blog(request):
    return render (request, 'blog1.html')


def signup_page(request):
    
    if request.method == "POST":
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        
        user = User.objects.filter(username = username)

        if user.exists():
            messages.error(request, 'Username already Exist!')
            return redirect('/signup_page')
        
        user = User.objects.create(
                email = email, 
                username = username,
                first_name = first_name,
                last_name = last_name,
            
        )
        user.set_password(password)
        user.save()
        print(f"{user.first_name} Your account has been created Successfully!")
        messages.success(request, f"Hello {first_name}, Your account has been created Successfully!")
        return redirect('/signup_page')

    return render (request, 'signup.html')


# LOGIN
def login_page(request):
    
    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']
        
        if not User.objects.filter(username = username).exists():
            messages.error(request, "Invalid Username!")
            return redirect('/login_page')

        user = authenticate(username = username, password = password)
    
        if user is None:
            messages.error(request, "Incorrect Password!")
            return redirect('/login_page')
        else:
            login(request, user)
            return redirect('/registration')
            
    return render (request, 'login.html')


# LOGOUT
def logout_page(request):

    logout(request)
    return redirect('/login_page')



#CRUD Operation

@login_required(login_url='/login_page')

def registration(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            user_obj = form.cleaned_data
            name = user_obj['name']
            email = user_obj['email']
            contact = user_obj['contact']
            address = user_obj['address']
            skills = user_obj['skills']
            marital_status = user_obj['marital_status']
            department = user_obj['department']
            position = user_obj['position']
            
            data = Employees(name = name,
                            email = email,
                            contact = contact,
                            address = address,
                            skills = skills,
                            marital_status = marital_status,
                            department = department,
                            position = position,)
            data.save()
            forms = EmployeeForm()
            print(name, email, contact, address, skills, marital_status, department, position)
            messages.success(request, f'{name} has been added to the dashboard successfully.')
            return redirect('/dashboard')
    else:
        forms = EmployeeForm()
        # employee = Employees.objects.all()
        
    return render (request, 'registration.html', {'forms':forms} ) 



@login_required(login_url='/login_page')
def dashboard(request):
    forms = EmployeeForm()
    employee = Employees.objects.all()

    context = {'forms':forms, 'employee': employee }
    return render (request, 'dashboard.html', context)


#UPDATE
@login_required(login_url='/login_page')

def update(request, id):

    employee = Employees.objects.get(id = id)
    form = EmployeeForm(instance = employee)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance = employee)
        if form.is_valid():
            form.save()
            return redirect('/dashboard')
    
    context = {'form':form}
    messages.success(request, 'Updation Complete.')
    return render (request, 'update.html', context)


# DELETE
def delete(request, id):
    
    query_set = Employees.objects.get(id = id)
    query_set.delete()
    messages.success(request,  f" {query_set.name} is Deleted!")
    return redirect('/dashboard')


def feedback(request):
    if request.method == 'POST':
        form = form.clea
    return render(request, 'feedback.html')