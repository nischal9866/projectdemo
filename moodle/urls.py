from django.contrib import admin
from django.urls import path
from .views import *
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'students',StudentViewset,basename='students')
router.register(r'courses',CourseViewset,basename='courses')
router.register(r'enrollments',EnrollmentViewset,basename='enrollments')
router.register(r'sponsors',SponsorshipViewset,basename='sponsors')
router.register(r'assignments',AssignmentViewset,basename='assignments')
router.register(r'admindashboard', AdminDashboardViewSet, basename='admindashboard')
router.register(r'sponsordashboard', SponsorDashboardViewSet, basename='sponsordashboard')
router.register(r'progressreport', ProgressReportViewset, basename='progressreport')
router.register(r'coursestatus', CourseStatusViewset, basename='coursestatus')

urlpatterns = [
    
]+router.urls
