from django.db import models

# Part: have part number, name of the part, status, created at, and updated at
# Things that in the airplane


class Part(models.Model):
    STATUS_CHOICES = [
        ("PROPOSED", "Proposed"),
        ("APPROVED", "Approved"),
        ("DEPRECATED", "Deprecated"),
    ]

    part_number = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="PROPOSED")
    created_at = models.DateTimeField(auto_now_add=True)   # set once on create
    updated_at = models.DateTimeField(auto_now=True)       # updates on save

    def __str__(self):
        return f"{self.part_number} - {self.name}"


class WorkItem(models.Model):
    PRIORITY_CHOICES = [
        ("HIGH", "High"),
        ("MEDIUM", "Medium"),
        ("LOW", "Low"),
    ]

    part = models.ForeignKey(
        Part, on_delete=models.CASCADE, related_name="work_items")
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    priority = models.CharField(
        max_length=15, choices=PRIORITY_CHOICES, default="MEDIUM")
    due_date = models.DateField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} for {self.part.part_number}"
