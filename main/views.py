from django.shortcuts import render
from .models import *
from .forms import TodoForm
# Create your views here.

def homepage(request):
   
    return render(request,'index.html')

def todo(request):
    
    if request.method == 'GET':
        form = TodoForm()
        
    elif request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            
            Todo.objects.create(**form.cleaned_data) 

            # return redirect('index')
    return render(request, 'todo.html', {'form':form})
    
def display(request):
    td = Todo.objects.all()

    return render(request,'display.html',{'td': td})
