from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from login.models import LoginUser
# Create your models here.

class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,limit_choices_to={'role': 'student'})
    
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('completed', 'Completed'),
        ('dropped', 'Dropped'),
    ]

    bio = models.TextField(blank=True, null=True)
    progress = models.PositiveIntegerField(default=0)  # 0 to 100
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')


    def __str__(self):
        return self.user.username
    
class Course(models.Model):
    DIFFICULTY_CHOICES = [
        ('BEGINNER', 'Beginner'),
        ('INTERMEDIATE', 'Intermediate'),
        ('ADVANCED', 'Advanced'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    difficulty = models.CharField(max_length=12, choices=DIFFICULTY_CHOICES)
    instructor = models.ForeignKey(LoginUser, on_delete=models.CASCADE, limit_choices_to={'role': 'instructor'})
    made_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.title} ----------------- Difficulty level:{self.difficulty} ------------------- Tutored By:{self.instructor}"

class Enrollment(models.Model):
    student = models.ForeignKey(LoginUser, on_delete=models.CASCADE, limit_choices_to={'role': 'student'})
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateField()
    progress = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.student} ----------------- Course Taken:{self.course} ------------------- Enrollment Date:{self.enrollment_date}"

class Assignment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    write_assignment=models.CharField(max_length=1000,null=True,blank=True)
    due_date = models.DateTimeField()
    student = models.ForeignKey(LoginUser, on_delete=models.CASCADE, limit_choices_to={'role': 'student'},null=True,blank=True) 
    def __str__(self):
        return f"Subject:{self.course}-----Assignment:{self.title}------Submission Date:{self.due_date}"


class Sponsorship(models.Model):
    sponsor = models.ForeignKey(LoginUser, on_delete=models.CASCADE, limit_choices_to={'role': 'sponsor'},related_name='sponsored_students')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    student = models.ForeignKey(LoginUser,on_delete=models.CASCADE, limit_choices_to={'role': 'student'},related_name='sponsors',null=True)
    sponsorship_impact=models.CharField(max_length=500,null=True,blank=True)
    def __str__(self):
        return f"{self.sponsor} ----------------- Sponsored to:{self.student} ------------------- Amount Funded:{self.amount}"
    
class ProgressReport(models.Model):
    student = models.ForeignKey(LoginUser,on_delete=models.CASCADE, limit_choices_to={'role': 'student'},null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    progress_percent = models.FloatField()
    last_updated = models.DateTimeField(auto_now=True)
    remarks = models.TextField(max_length=1000,blank=True)
    def __str__(self):
        return f"Progress for {self.student} in {self.course}"
    
class CourseStatus(models.Model):
    COURSE_STATUS = [
        ('COMPLETED', 'Completed'),
        ('INACTIVE', 'Inactive'),
        ('RUNNING', 'Running'),
    ]
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    status=models.CharField(max_length=12, choices=COURSE_STATUS)
    completion_rate=models.FloatField(null=True,default=0)
    message=models.CharField(max_length=200)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Updation in Course Competion Rate of {self.course}"