from django.urls import URLPattern, path
from . import views

URLPattern = [
    path('encontrar_jobs/', views.encontrar_jobs, name="encontrar_jobs")
]