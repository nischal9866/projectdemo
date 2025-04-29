from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'progress')
    search_fields = ('user__username',)

admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(Assignment)
admin.site.register(Sponsorship)
admin.site.register(ProgressReport)
admin.site.register(CourseStatus)

