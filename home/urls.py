from django.urls import path

from . import views
from .views import TaskCreateView, TaskDeleteView, TaskUpdateView, TaskListView

urlpatterns = [
    path('', views.index, name='index'),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/add/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/edit/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
]


app_name = "home-app"