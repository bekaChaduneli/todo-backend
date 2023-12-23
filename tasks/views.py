from django.http import HttpResponse, JsonResponse
from django.views import View
from rest_framework import viewsets
from .serializers import TaskSerializer
from .models import Task
from .pagination import TasksPagination
from .filters import TaskFilter
# Create your views here.

class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    pagination_class = TasksPagination
    filterset_class = TaskFilter

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
