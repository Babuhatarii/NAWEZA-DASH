from django.http import HttpResponse
from .models import Activity, Enrollment, Progress
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


def landing_page(request):
    """
    View function to render the landing page.
    """
    return render(request, 'landing.html')

def signin_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)

        return redirect('mydashboard_page')
    else:
        messages.error(request, 'Invalid username or password')
    return render(request, 'sign_in.html')

def createaccount_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect('createaccount_page')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken')
            return redirect('createaccount_page')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already registered')
            return redirect('createaccount_page')
        
        user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)    
        user.save()

        return redirect('signin_page')

    return render(request, 'create_account.html')

def mydashboard_page(request):
    #my dashboard view
    return render(request, 'dash.html')


def activity_detail(request, activity_id):
    """
    View function to display details of a specific activity.
    """
    activities = Activity.objects.all()
    """
    Generate a response containing the list of all activities
    """
    response = "\n".join([Activity.name for Activity in activities])

    """Return the response"""
    return HttpResponse(response)

    