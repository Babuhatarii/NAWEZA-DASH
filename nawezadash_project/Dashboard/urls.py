from django.urls import path
from .views import activity_detail, landing_page  # Import views

urlpatterns = [
    path('', landing_page, name='landing_page'),  # Root URL
    path('<int:activity_id>/', activity_detail, name='activity_detail'),  # Dynamic URL
]
