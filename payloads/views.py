from django.shortcuts import redirect, render, get_object_or_404

from django.http import HttpResponse
from .models import Part, WorkItem
from .forms import WorkItemForm
from datetime import date, timedelta


# Create your views here.
def home(request):
    return redirect("parts_list")


def dashboard(request):
    today = date.today()
    soon = today + timedelta(days=7)
    total_parts = Part.objects.count()
    total_work_items = WorkItem.objects.count()
    high_priority_count = WorkItem.objects.filter(priority="HIGH").count()
    due_soon_count = WorkItem.objects.filter(
        due_date__gte=today,
        due_date__lte=soon,
    ).count()

    context = {
        "total_parts": total_parts,
        "total_work_items": total_work_items,
        "high_priority_count": high_priority_count,
        "due_soon_count": due_soon_count,
        "today": today,
        "soon": soon,

    }

    return render(request, "payloads/dashboard.html", context)


def parts_list(request):
    parts = Part.objects.all().order_by("part_number")
    context = {"parts": parts}
    return render(request, "payloads/parts_list.html", context)


def part_detail(request, pk):
    part = get_object_or_404(Part, pk=pk)
    work_items = part.work_items.all().order_by("due_date")

    if request.method == "POST":
        form = WorkItemForm(request.POST)
        if form.is_valid():
            work_item = form.save(commit=False)
            work_item.part = part  # attach this work item to the current part
            work_item.save()
            return redirect("part_detail", pk=part.pk)
    else:
        form = WorkItemForm()

    context = {
        "part": part,
        "work_items": work_items,
        "form": form,
    }
    return render(request, "payloads/part_detail.html", context)
