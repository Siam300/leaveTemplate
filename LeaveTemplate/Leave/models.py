from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

class LeaveRequest(models.Model):
    APPROVAL_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('declined', 'Declined'),
    ]

    student = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    approval_status = models.CharField(max_length=20, choices=APPROVAL_CHOICES, default='pending')
    email = models.EmailField(default='example@example.com')

    def __str__(self):
        return f"{self.student.username} - {self.start_date} to {self.end_date} ({self.approval_status})"
