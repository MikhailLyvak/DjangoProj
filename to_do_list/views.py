from typing import Any, Dict
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from .models import Tag, Task
from .forms import TaskCreateForm


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 3
    

class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("to_do_list:tags-list")
    

class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("to_do_list:tags-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("to_do_list:tags-list")


class TaskListView(generic.ListView):
    model = Task
    paginate_by = 3
    

class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskCreateForm
    success_url = reverse_lazy("to_do_list:tasks-list")
    

class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskCreateForm
    success_url = reverse_lazy("to_do_list:tasks-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("to_do_list:tasks-list")
    
def update_is_done(request, pk=None):
    if request.method == "POST" and pk is not None:
        task = Task.objects.get(pk=pk)
        task.done = not task.done
        task.save()
    return redirect("to_do_list:tasks-list")
