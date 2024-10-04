from django.urls import path, include

from apps.project.models.project import Project
from apps.project.views.project_views import ProjectsApi

urlpatterns = [
    path('',ProjectsApi.as_view()),
    path('project/', include('apps.project.urls')),
]