from django.urls import path
from infoschoolpupil.views import all_info

urlpatterns = [
    path('', all_info)
]