from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from .models import Food
from .forms import FoodForm
# Create your views here.
def index(request):
    foods = Food.objects.all()
    template = loader.get_template("index.html")
    context = {'foods':foods}
    return HttpResponse(template.render(context, request))

def delete(request, id):
    food = Food.objects.get(pk=id)
    print("checked")
    if request.method == 'POST':
        food.delete()
        return redirect("food:index")
    
    template = loader.get_template("delete.html")
    context = {
        "food" : food
    }
    return HttpResponse(template.render(context, request))

def add(request):
    if request.method == 'POST':
        form = FoodForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("food:index")
    form = FoodForm()   
    template = loader.get_template("form.html")
    context = {
        'form':form
    }
    return HttpResponse(template.render(context, request))

def update(request, id):
    food = Food.objects.get(pk=id)
    if (request.method == 'POST'):
        form = FoodForm(request.POST, request.FILES, instance=food)
        if form.is_valid():
            form.save()
            return redirect('food:index')
        
    form = FoodForm(instance=food)
    template = loader.get_template("form.html")
    context = {
        'form':form
    }
    return HttpResponse(template.render(context, request))
