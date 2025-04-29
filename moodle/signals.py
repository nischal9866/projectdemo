from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *
from django.core.mail import send_mail

@receiver(post_save,sender=Enrollment)
def enrollment_update(sender,instance,**kwargs):
    print("Student has enrolled")
    send_mail(
        subject="Enrollment Message",
        message="Welcome to our course.Contact your instructor for more information . Best of luck for your future",
        from_email='admin@gmail.com',
        recipient_list=('student@gmail.com',)
    )

@receiver(post_save,sender=Course)
def course(sender,instance,**kwargs):
    print("Course was updated by instructor")
    send_mail(
        subject="Course completion and Assessment Updates",
        message="Dear Students, Our Course is about to end . Please submit your assignment within tommorrow ",
        from_email='admin@gmail.com',
        recipient_list=('student@gmail.com',)
    )
@receiver(post_save,sender=Sponsorship)
@receiver(post_save,sender=ProgressReport)
def progress_update(sender,instance,**kwargs):
    print("Progress updated")
    send_mail(
        subject="Progress reports and student results update",
        message="Dear Sponsors, We have updated our students progress and improvements.Kindly visit to sponsors dashboard to view the updates ",
        from_email='admin@gmail.com',
        recipient_list=('sponsor@gmail.com',)
    )

@receiver(post_save,sender=Assignment)
def on_assignment_given(sender,instance,**kwargs):
    print("Assignment Added")
    send_mail(
        subject="New Assignment and upcoming deadlines",
        message="Dear Students, Assignment has been added and updated by instructors, Please submit within the given deadline for better grades",
        from_email='admin@gmail.com',
        recipient_list=('student@gmail.com',)
    )

@receiver(post_save,sender=Enrollment)
def on_enrollmentinstructor(sender,instance,**kwargs):
    print("Student Engaged")
    send_mail(
        subject="Enrollments of students",
        message="Dear Instructors, student has been enrolled in our course. We request you to take care of their studies",
        from_email='admin@gmail.com',
        recipient_list=('instructor@gmail.com',)
    )

@receiver(post_save,sender=CourseStatus)
def on_coursecompletionrates(sender,instance,**kwargs):
    print("Course Completion Rate Updated")
    send_mail(
        subject="Updation on course completion rates",
        message="Dear Instructors, There has been updates in course completion rates, Kindly check the course site to view the update rates",
        from_email='admin@gmail.com',
        recipient_list=('instructor@gmail.com',)
    )