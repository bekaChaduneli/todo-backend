from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
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


    # @action(detail=False, methods=['delete'])
    # def delete_completed(self, request):
    #     completed_tasks = self.get_queryset().filter(completed=True)
    #     completed_tasks.delete()
    #     return Response({"detail": "Completed tasks deleted successfully."})