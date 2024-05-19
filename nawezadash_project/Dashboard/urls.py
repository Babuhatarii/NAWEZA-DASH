from django.urls import path, re_path
from .views import landing_page, signin_page, createaccount_page, mydashboard_page, list_activities # Import views

urlpatterns = [
    path('', landing_page, name='landing_page'),  # Root URL
    path('signin/', signin_page, name='signin_page'),  # Signin page URL
    path('create-account/', createaccount_page, name='createaccount_page'),
    path('member dashboard/', mydashboard_page, name='mydashboard_page'),
    path('activities', list_activities, name='list_activities')
    #path('activities/<int:activity_id>/', activity_detail, name='activity_detail'),
]
