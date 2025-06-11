from rest_framework.routers import DefaultRouter
from .views import TasksList
from django.urls import path, include

router = DefaultRouter()
router.register(r'tasks', TasksList, basename='tasks')

urlpatterns = [
    path('', include(router.urls)),
]

