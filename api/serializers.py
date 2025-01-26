from rest_framework import serializers
from todo.models import Task
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id','username']

class TaskSerialiazer(serializers.ModelSerializer):
    
    class Meta:
        model = Task
        fields = ['id','title','description' , 'completed']
     
    def validate_title(self, value):
        """Check that the title is not empty."""
        if not value:
            raise ValidationError("Title cannot be empty.")
        return value

    def validate(self, attrs):
        """Additional validation for the entire object."""
        if attrs.get('completed') and not attrs.get('title'):
            raise ValidationError("If the task is completed, a title must be provided.")
        return attrs

    def create(self, validated_data):
        """Custom create method to handle additional logic if needed."""
        try:
            task = Task.objects.create(**validated_data)
            return task
        except Exception as e:
            raise ValidationError(f"Error creating task: {str(e)}")

    def update(self, instance, validated_data):
        """Custom update method to handle additional logic if needed."""
        try:
            instance.title = validated_data.get('title', instance.title)
            instance.description = validated_data.get('description', instance.description)
            instance.completed = validated_data.get('completed', instance.completed)
            instance.save()
            return instance
        except Exception as e:
            raise ValidationError(f"Error updating task: {str(e)}")   
    
        
        

    