from rest_framework.permissions import BasePermission,SAFE_METHODS

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role == 'admin'
    
class IsStudentEnrollCourse(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role == 'student'

class IsInstructor(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role == 'instructor' 

class IsStudentCanReadCourse(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role == 'student' and request.method in SAFE_METHODS 

class IsStudentCanUpdateAssignment(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 'student' and request.method in ['POST', 'DELETE']:
            return False
        return True  
    def has_object_permission(self, request, view, obj):
        if request.user.role == 'student' and request.method in ['PUT', 'PATCH']:
            return True  

        return True 

class IsSponsorReadOnlyStudent(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role == 'sponsor' and request.method in SAFE_METHODS
    
class IsInstructorReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role == 'instructor' and request.method in SAFE_METHODS
    
