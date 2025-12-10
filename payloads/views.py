from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from .models import Part

# Create your views here.


def parts_list(request):
    parts = Part.objects.all().order_by("part_number")
    context = {"parts": parts}
    return render(request, "payloads/parts_list.html", context)


def part_detail(request,pk):
    part = get_object_or_404(Part, pk=pk)
    work_items = part.work_items.all().order_by("due_date")
    context = {
        "part":part,
        "work_items":work_items
    }
    return render(request, "payloads/part_detail.html", context)
