from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Food
# Create your views here.
def index(request):
    foods = Food.objects.all()
    template = loader.get_template("index.html")
    context = {'foods':foods}
    return HttpResponse(template.render(context, request))