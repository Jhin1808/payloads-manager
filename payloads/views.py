from django.shortcuts import render
from django.http import HttpResponse
from .models import Part
# Create your views here.


def parts_list(request):
    parts = Part.objects.all().order_by("part_number")
    context = {"parts": parts}
    return render(request, "payloads/parts_list.html", context)
