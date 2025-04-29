from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.serializers import ValidationError
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView,ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework import viewsets,response
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
from .permissions import *
from .filters import *
from django_filters import rest_framework as filter
# from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.
class StudentViewset(viewsets.ModelViewSet):
    """
    Student Records
    """
    queryset=Student.objects.all()
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAdmin|IsSponsorReadOnlyStudent]
    serializer_class= StudentSerializer
    pagination_class=PageNumberPagination
    filter_backends=[filters.SearchFilter,filter.DjangoFilterBackend]
    filterset_class=StudentFilter
    search_fields=['progress','status']


class CourseViewset(viewsets.ModelViewSet):   
 
    queryset=Course.objects.all()
    serializer_class=CourseSerializer
    authentication_classes=[TokenAuthentication]
    pagination_class=PageNumberPagination
    filter_backends=[filters.SearchFilter,filter.DjangoFilterBackend]
    filterset_class=CourseFilter
    search_fields=['title','difficulty','instructor__username']
    permission_classes=[IsInstructor|IsStudentCanReadCourse|IsAdmin]

    def destroy(self,request,*args,**kwargs):
        courses=self.get_object()
        enrollment=Enrollment.objects.filter(course=courses).count()
        assignment=Assignment.objects.filter(course=courses).count()
        if enrollment>0:
            raise ValidationError({
                "details":"Students are already enrolled in this course. Hence, Course cant be deleted"
            })
        
        if assignment>0:
            raise ValidationError({
                "details":"Assignments are already given from this course. Hence, Course cant be deleted"
            })
        courses.delete()
        return Response({
            "details":"Course has been removed"
        },status=status.HTTP_204_NO_CONTENT)


class EnrollmentViewset(viewsets.ModelViewSet):
    """
    Feel free to enroll in our courses
    """   
    queryset=Enrollment.objects.all()
    authentication_classes=[TokenAuthentication]
    serializer_class=EnrollmentSerializer
    pagination_class=PageNumberPagination
    permission_classes=[IsAdmin|IsSponsorReadOnlyStudent|IsStudentEnrollCourse]
    def destroy(self, request, *args, **kwargs):
        enrollments=self.get_object()
        students=Student.objects.filter(enrollment=enrollments).count()
        if students>0:
            raise ValidationError({
                "details":"Students are already enrolled"
            },status=status.HTTP_204_NO_CONTENT)
        enrollments.delete()

class SponsorshipViewset(viewsets.ModelViewSet):    
    queryset=Sponsorship.objects.all()
    authentication_classes=[TokenAuthentication]
    pagination_class=PageNumberPagination
    serializer_class=SponsorSerializer
    permission_classes=[IsSponsorReadOnlyStudent|IsAdmin]

class AssignmentViewset(viewsets.ModelViewSet):
    """
    Dear Students, Please complete your assignment within the deadline for upgrading the semester
    """
    queryset=Assignment.objects.all()
    authentication_classes=[TokenAuthentication]
    serializer_class=AssignmentSerializer
    permission_classes=[IsInstructor|IsStudentCanUpdateAssignment|IsAdmin]
    pagination_class=PageNumberPagination

class ProgressReportViewset(viewsets.ModelViewSet):
    queryset=ProgressReport.objects.all()
    authentication_classes=[TokenAuthentication]
    serializer_class=ProgressReportSerializer
    permission_classes=[IsAdmin|IsSponsorReadOnlyStudent]

class CourseStatusViewset(viewsets.ModelViewSet):
    queryset=CourseStatus.objects.all()
    authentication_classes=[TokenAuthentication]
    serializer_class=CourseStatusSerializer
    permission_classes=[IsInstructorReadOnly|IsAdmin]

class AdminDashboardViewSet(viewsets.ViewSet):
    """
    Overall view for the admin
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdmin]
    pagination_class=PageNumberPagination

    def list(self, request):
        user = request.user

        students = Student.objects.all()
        instructors = LoginUser.objects.filter(role='instructor')
        courses = Course.objects.all()
        enrollments = Enrollment.objects.all()

        data = {
            "Greetings": f"Hi {user.username}",
            "Students": StudentSerializer(students, many=True).data,
            "Instructors": InstructorSerializer(instructors, many=True).data,
            "Active Courses": CourseSerializer(courses, many=True).data,
            "Enrollments": EnrollmentSerializer(enrollments, many=True).data,
        }

        return response.Response(data, status=status.HTTP_200_OK)
    
class SponsorDashboardViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Sponsor dashboard:
    - List all students 
    - Get summary analytics of the sponsored students
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdmin|IsSponsorReadOnlyStudent]
    def list(self, request):
        user = request.user
        sponsors=Sponsorship.objects.all()
        student=Student.objects.all()
        progress=ProgressReport.objects.all()
        data={
            "Greetings":f"Hi {user.username}. Thanks for supporting us and our students",
            "Sponsorship":SponsorSerializer(sponsors,many=True).data,
            "Students":StudentSerializer(student,many=True).data,
            "Progress Report":ProgressReportSerializer(progress,many=True).data,

        }
        return response.Response(data, status=status.HTTP_200_OK)
