from django.db import models  

from django.db import models
from django.contrib.auth import get_user_model

####################################

User = get_user_model()

class Task(models.Model): 
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)  
    description = models.TextField()  
    due_date = models.DateTimeField(null= True , blank=True)  
    completed = models.BooleanField(default=False)  
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)  

    def __str__(self):  
        return self.title