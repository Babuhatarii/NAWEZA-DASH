from django.urls import path, re_path
from .views import activity_detail, landing_page, signin_page # Import views

urlpatterns = [
    path('', landing_page, name='landing_page'),  # Root URL
    path('signin/', signin_page, name='signin_page'),  # Signin page URL
    path('<int:activity_id>/', activity_detail, name='activity_detail'),  # Dynamic URL
]
