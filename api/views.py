from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters

from django_filters.rest_framework import DjangoFilterBackend

from todo.models import Task
from .serializers import TaskSerialiazer

# Create your views here.

class TaskListAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerialiazer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['completed','due_date','created_at'] 
    ordering_fields = ['created_at']  
    ordering = ['created_at']    
    search_fields = ['title', 'description']

    def get_queryset(self):
        user = self.request.user
        queryset = Task.objects.filter(user=user)
        return queryset
    
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TaskDetailAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerialiazer

    def get_queryset(self):
        
        user = self.request.user
        queryset = Task.objects.filter(user=user)
        return queryset

    




    
    
    
    
    

