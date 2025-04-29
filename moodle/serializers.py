from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True) 
    class Meta:
       model=Student
       fields=('id','username','bio','progress','status')

class CourseSerializer(serializers.ModelSerializer):
    instructor = serializers.CharField(source='instructor.username', read_only=True)
    class Meta:
        model=Course
        fields=('id','title','description','difficulty','instructor')
    

class EnrollmentSerializer(serializers.ModelSerializer):
    # student=serializers.StringRelatedField()
    class Meta:
        model=Enrollment
        fields='__all__'
class SponsorSerializer(serializers.ModelSerializer):
    student=serializers.StringRelatedField()
    sponsor=serializers.StringRelatedField()
    class Meta:
        model=Sponsorship
        fields='__all__'
class AssignmentSerializer(serializers.ModelSerializer):
    # course=serializers.StringRelatedField()
    class Meta:
        model=Assignment
        fields='__all__'

class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginUser
        fields = ['id', 'username', 'email', 'role']

class ProgressReportSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProgressReport
        fields='__all__'

class CourseStatusSerializer(serializers.ModelSerializer):
    course=serializers.StringRelatedField()
    class Meta:
        model=CourseStatus
        fields='__all__'