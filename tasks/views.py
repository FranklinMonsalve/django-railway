from django.shortcuts import render
from rest_framework import viewsets
from .models import Task
from .serializer import TaskSerializer


# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()  # Replace with your Task model queryset
    serializer_class = TaskSerializer  # Replace with your Task model serializer