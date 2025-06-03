from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList
from .forms import CreateNewList

# Create your views here.
"""def about(response):
    return HttpResponse("<h1>About Us</h1><p>This is the about page.</p>")

def index(response, name):
    ls = ToDoList.objects.get(name=name)
    items = ls.item_set.get(id=1)
    return HttpResponse("<h1>%s</h1><br></br><p>%s</p>" % (ls.name, str(items.text)))
"""
def home(response):
    return render(response, "main/home.html")

def index(response):
    return render(response, "main/list.html")

def create(response):
    form = CreateNewList()
    return render(response, "main/create.html", {"form":form})

