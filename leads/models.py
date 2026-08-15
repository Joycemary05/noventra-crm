from django.db import models
from django.contrib.auth.models import User

class Lead(models.Model):

    STATUS_CHOICES = [
        ('new', 'New'),
        ('contacted', 'Contacted'),
        ('converted', 'Converted'),
    ]

    SOURCE_CHOICES = [
        ('website', 'Website'),
        ('linkedin', 'LinkedIn'),
        ('instagram', 'Instagram'),
        ('referral', 'Referral'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    company = models.CharField(max_length=100, blank=True)
    source = models.CharField(
        max_length=20,
        choices=SOURCE_CHOICES,
        default='website'
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='new'
    )
    message = models.TextField(blank=True, null=True)

    assigned_to = models.ForeignKey(
    User,
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name="assigned_leads"
)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class FollowUp(models.Model):
    lead = models.ForeignKey(
        Lead,
        on_delete=models.CASCADE,
        related_name='followups'
    )
    note = models.TextField()
    follow_up_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.lead.name} - {self.follow_up_date}"