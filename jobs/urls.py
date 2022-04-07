from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('encontrar_jobs/', views.encontrar_jobs, name="encontrar_jobs")
]