from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from .models import Food
# Create your views here.
def index(request):
    foods = Food.objects.all()
    template = loader.get_template("index.html")
    context = {'foods':foods}
    return HttpResponse(template.render(context, request))

def delete(request, id):
    food = Food.objects.get(pk=id)

    if request.method == 'POST':
        food.delete()
        return redirect("food:index")
    
    template = loader.get_template("delete.html")
    context = {
        "food" : food
    }
    return HttpResponse(template.render(context, request))