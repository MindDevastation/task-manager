from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from home.models import Task, Worker


# Create your views here.

def index(request):

    context = {}

    # Add context data here
    # context['test'] = 'OK'

    # Page from the theme 
    return render(request, "pages/dashboard.html", context=context)

class TaskListView(ListView):
    model = Task
    template_name = "pages/task_list.html"
    context_object_name = "tasks"

    def get_queryset(self):
        if self.request.user.is_authenticated:
            worker = self.request.user.id

            return Task.objects.filter(assignees=worker)
        else:
            return Task.objects.none()

class TaskCreateView(CreateView):
    model = Task
    fields = ["name", "description", "deadline", "is_completed", "priority", "task_type", "assignees"]
    template_name = "pages/task_form.html"
    success_url = reverse_lazy("home-app:task-list")


class TaskUpdateView(UpdateView):
    model = Task
    fields = ["name", "description", "deadline", "is_completed", "priority", "task_type", "assignees"]
    template_name = "pages/task_form.html"
    success_url = reverse_lazy("home-app:task-list")


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "pages/task_confirm_delete.html"
    success_url = reverse_lazy("home-app:manager:task-list")
