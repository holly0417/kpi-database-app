from django.http import JsonResponse
from .models import KPI, GICSSector

from django.shortcuts import render

# Create your views here.
def home(request):
    # You can pass data to the template here
    return render(request, "home.html")

def gics_sector_list_api(request):
    data = [
        {
            "code": gs.code,
            "name": gs.name,
        }
        for gs in GICSSector.objects.all()
    ]
    return JsonResponse(data, safe=False)

def kpi_list_api(request):
    data = [
        {
            "id": k.id,
            "name": k.name,
            "unit": k.unit,
            "direction": k.direction,
        }
        for k in KPI.objects.all()
    ]
    return JsonResponse(data, safe=False)