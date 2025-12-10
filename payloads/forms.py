from django import forms
from .models import WorkItem


class WorkItemForm(forms.ModelForm):
    class Meta:
        model = WorkItem
        fields = ["title", "description", "priority", "due_date"]
