from django.urls import path
from .views import ProfileList  # Ensure the view is imported with the correct name

urlpatterns = [
    path('profiles/', ProfileList.as_view(), name='profile_list'),  # Correct reference
]
