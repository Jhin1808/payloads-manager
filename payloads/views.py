from django.shortcuts import redirect, render, get_object_or_404

from django.http import HttpResponse
from .models import Part
from .forms import WorkItemForm


# Create your views here.
def home(request):
    return redirect("parts_list")


def dashboard(request):
    return HttpResponse("Dashboard template")


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
