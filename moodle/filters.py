from django_filters import rest_framework as filter
from .models import *
class CourseFilter(filter.FilterSet):
    class Meta:
        model=Course
        fields={
            'title':['exact'],
            'difficulty':['exact'],
            'instructor':['exact']
        }
    
class StudentFilter(filter.FilterSet):
    class Meta:
        model=Student
        fields={
            'status':['exact'],
            'progress':['exact']
            
        }