from rest_framework import viewsets

from tasks.models import ToDoList
from tasks.serializer import ToDoLIstSerializer


class TasksList(viewsets.ModelViewSet):
    queryset = ToDoList.objects.all()
    serializer_class = ToDoLIstSerializer

