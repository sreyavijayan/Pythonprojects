from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import task
from .forms import todoform
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import DeleteView
from django.views.generic import UpdateView


# Create your views here.

class tasklistview(ListView):
    model = task
    template_name = 'home.html'
    context_object_name = 'task2'


class taskdetailview(DetailView):
    model = task
    template_name = 'detail.html'
    context_object_name = 'task3'


class taskupdateview(UpdateView):
    model = task
    template_name = 'updateview.html'
    context_object_name = 'task3'
    fields = ['name', 'prio', 'date1']

    def get_success_url(self):
        return reverse_lazy('cbvdetail')
        # return reverse_lazy('cbvdetail', kwargs={'pk'self.object.id})


class taskdeleteview(DetailView):
    model = task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')


def home(request):
    if request.method == 'POST':
        name = request.POST.get('task', '')
        prio = request.POST.get('priority', '')
        date1 = request.POST.get('date1', '')
        task1 = task(name=name, prio=prio, date1=y)
        task1.save()
    task2 = task.objects.all()
    return render(request, 'home.html', {'task2': task2})


def delete(request, taskid):
    if request.method == 'POST':
        task1 = task.objects.get(id=taskid)
        task1.delete()
        return redirect('/')

    return render(request, 'delete.html')


def update(request, taskid):
    task1 = task.objects.get(id=taskid)
    f1 = todoform(request.POST or None, instance=task1)
    if f1.is_valid():
        f1.save()
        return redirect('/')
    return render(request, 'update.html', {'f1': f1, 'task1': task1})
