from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class LoginUser(AbstractUser):
    phone_number=models.CharField(max_length=10,null=True,blank=True)
    USERNAME_FIELD = "username"
    ROLE_CHOICES=(
       ('admin','Admin'),
       ('instructor','Instructor'),
       ('student','Student'),
       ('sponsor','Sponsor'),
                )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES,default='student')
    def __str__(self):
      return f"{self.username} : {self.role}" 