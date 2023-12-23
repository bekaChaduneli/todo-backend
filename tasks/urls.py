from django.urls import path, include
from .views import TaskView
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'', TaskView, 'task')

urlpatterns = [
    path('', include(router.urls)),
]