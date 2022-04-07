from django.shortcuts import render
from .models import Jobs
from django.http import HttpResponse

def encontrar_jobs(request):
    if request.method == "GET":
        preco_minimo = request.GET.get('preco_minimo')
        preco_maximo = request.GET.get('preco_maximo')

        prazo_minimo = request.GET.get('prazo_minimo')
        prazo_maximo = request.GET.get('prazo_maximo')

        categoria = request.GET.get('categoria')

        jobs = Jobs.objects.filter(reservado=False)
        return render(request, 'encontrar_jobs.html', {'jobs': jobs})
