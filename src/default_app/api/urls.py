"""
    ToDo: DocString
"""
from django.urls import path
from .system_management.people_api_views import (
    people_crud_api_view, person_read_api_view)


system_management_patterns = [
    path("system/people/", people_crud_api_view),
    path("system/people/<str:uid>", person_read_api_view)
]


urlpatterns = system_management_patterns
