from django.http import HttpResponse
from .models import Activity, Enrollment, Progress
from django.shortcuts import render, redirect

def landing_page(request):
    """
    View function to render the landing page.
    """
    return render(request, 'landing.html')

def signin_page(request):
    """
    view function o render the sign in page.
    """
    return render(request, 'sign_in.html')

def createaccount_page(request):
    return render(request, 'create_account.html')

def mydashboard(request):
    #my dashboard view
    return render(request, 'mydashboard.html')


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

    