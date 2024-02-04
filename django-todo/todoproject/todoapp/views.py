from django.shortcuts import render,redirect
from .models import*
from .forms import*
from django.views import View

# Create your views here.

def index(request):
    if request.method == "POST":
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            todo_list = Todos.objects.all
            return render(request,'index.html',{"name":"AUP","todo_list":todo_list})            
    else:
        todo_list = Todos.objects.all
        return render(request,'index.html',{"name":"AUP","todo_list":todo_list})

def about(request):
    return render(request,'about.html')

def create(request):
    if request.method == "POST":
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            todo_list = Todos.objects.all
            return render(request,'create.html',{"name":"AUP Tech","todo_list":todo_list})            
    else:
        todo_list = Todos.objects.all
        return render(request,'create.html',{"name":"AUP Tech","todo_list":todo_list})
    
    
def delete(request,Todos_id):
    todo = Todos.objects.get(pk=Todos_id)
    todo.delete()
    return redirect("index")


def finished(request,Todos_id):
    todo = Todos.objects.get(pk=Todos_id)
    todo.finished = False
    todo.save()
    return redirect("index")


def notfinished(request,Todos_id):
    todo = Todos.objects.get(pk=Todos_id)
    todo.finished = True
    todo.save()
    return redirect("index")


def update(request,Todos_id):
    if request.method == "POST":
        todo_list = Todos.objects.get(pk=Todos_id)
        form = ListForm(request.POST or None,instance=todo_list)
        if form.is_valid():
            form.save()
            return redirect("index")          
    else:
        todo_list = Todos.objects.all
        return render(request,"update.html",{"todo_list":todo_list})