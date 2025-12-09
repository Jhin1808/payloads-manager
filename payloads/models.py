from django.db import models

# Create your models here.
#Part: have part number, name of the part, status, created at, and updated at
class Part(models.Model):
    STATUS_CHOICES = [
        ("PROPOSED", "Proposed"),
        ("APPROVED", "Approved"),
        ("DEPRECATED", "Deprecated"),
    ]
    
    part_number = models.CharField(max_length=50, unique = True)
    name = models.CharField(max_length=150)
    status = models.CharField(max_length=20, choices= STATUS_CHOICES, default= "PROPOSED")
    created_at = models.DateTimeField(auto_now_add=True)   # set once on create
    updated_at = models.DateTimeField(auto_now=True)       # updates on save


def __str__(self):
    return f"{self.part_number} - {self.name}"
