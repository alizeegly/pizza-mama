from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza

# Create your views here.

# /main
def index(request):
    '''
    pizzas = Pizza.objects.all()
    pizzas_nom = [pizza.nom + " : " + str(pizza.prix) + "€" for pizza in pizzas]
    pizzas_nom_str = ", ".join(pizzas_nom)
    return HttpResponse(f"Les Pizzas : {pizzas_nom_str}")
    '''

    pizzas = Pizza.objects.all().order_by('prix')
    return render(request, "menu/index.html", {
        "pizzas" : pizzas
    })