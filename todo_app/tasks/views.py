from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Create your views here.
@login_required(login_url="/users/login/")
def get_task(request):
	tasks = Task.objects.all()

	form = TaskForm()

	if request.method =='POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			print('form is valid')
			form.save()
		return redirect('tasks')


	data = {'tasks':tasks, 'form':form}
	return render(request, 'tasks.html', data)

def update_task(request, pk):
	task = Task.objects.get(id=pk)

	form = TaskForm(instance=task)

	if request.method == 'POST':
		form = TaskForm(request.POST, instance=task)
		if form.is_valid():
			form.save()
			return redirect('tasks')

	data = {'form':form}

	return render(request, 'update_task.html', data)

def delete_task(request, pk):
	item = Task.objects.get(id=pk)

	if request.method == 'POST':
		item.delete()
		return redirect('tasks')

	data = {'item':item}
	return render(request, 'delete_task.html', data)


