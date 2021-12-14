from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from ckeditor.fields import RichTextField
from PIL import Image



# Create your models here.

DeptChoice = [
    ('', 'Department'),
    ('Not Applicable', 'Not Applicable'),
    ('Mechanical', 'Mechanical'),
    ('Civil', 'Civil '),
    ('Electrical', 'Electrical'),
    ('Computer Science', 'Computer Science'),
    ('Electronics & Communication', 'Electronics & Communication'),
]
YearChoice = [
    ('', 'Year'),
    ('Not Applicable', 'Not Applicable'),
    ('First Year', 'First Year'),
    ('Second Year', 'Second Year '),
    ('Third Year', 'Third Year'),
    ('Fourth Year', 'Fourth Year'),
]
SemChoice = [
    ('', 'Semester'),
    ('Not Applicable', 'Not Applicable'),
    ('First Semester', 'First Semester'),
    ('Second Semester', 'Second Semester '),
    ('Third Semester', 'Third Semester'),
    ('Fourth Semester', 'Fourth Semester'),
    ('Fifth Semester', 'Fifth Semester'),
    ('Sixth Semester', 'Sixth Semester'),
    ('Seventh Semester', 'Seventh Semester'),
    ('Eightth Semester', 'Eightth Semester'),
]



NewsDeptChoice = [
    ('Mechanical', 'Mechanical'),
    ('Civil', 'Civil'),
    ('Electrical', 'Electrical'),
    ('ComputerScience', 'Computer Science'),
    ('Electronics&Communication', 'Electronics & Communication'),
    ('Event', 'Event'),
    ('CDC', 'CDC'),
    ('Sports', 'Sports'),
    ('Achievement', 'Achievement'),
]



class User(AbstractUser):
    # Need For All Project
    dept = models.CharField(
        max_length=40, choices=DeptChoice, default='Computer Science')
    year = models.CharField(
        max_length=40, choices=YearChoice, default='First Year')
    semester = models.CharField(
        max_length=40, choices=SemChoice, default='First Semester')
    enrollment = models.CharField(max_length=70, null=True, blank=True)
    profilepic = models.ImageField(
        upload_to='profile_pic/', null=True, blank=True, default='https://res.cloudinary.com/mern-commerce/image/upload/v1633459954/usericon_hpewnq.png')
    is_cdc = models.BooleanField('Is cdc', default=False)        
    is_teacher = models.BooleanField('Is teacher', default=False)
    is_student = models.BooleanField('Is student', default=False)
    status = models.BooleanField(default=True)




class News(models.Model):
    # Only For News Project

    headlines = models.TextField(max_length=100, null=True, blank=True)
    details = RichTextField(null=True, blank=True)
    img=models.ImageField(
        upload_to='news_pic/', null=True, blank=True, default='https://res.cloudinary.com/mern-commerce/image/upload/v1632004028/QuickShair/noimage_e5ohnw.jpg')
    
     
    
        
    
    
    
    dept = models.CharField(
        max_length=100, choices=NewsDeptChoice, default='Computer Science')
    owner = models.PositiveIntegerField(null=True, blank=True)
    status = models.BooleanField(default=False)
    postedtime = models.DateField(
        auto_now_add=False, auto_now=False, null=True, blank=True)

