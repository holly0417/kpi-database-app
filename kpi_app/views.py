import mimetypes

from django.http import JsonResponse, Http404, HttpResponse, FileResponse
from django.conf import settings
from pathlib import Path

from .models import KPI, GICSSector

from django.shortcuts import render

# Create your views here.
SPA_ROOT = Path(settings.BASE_DIR) / "frontend" / "dist" / "spa"

def spa_view(request, resource_path: str = ""):
    # Normalize the requested path (e.g. "js/app.js", "", "some/route")
    resource_path = resource_path.lstrip("/")

    # Candidate file under the SPA build directory
    candidate = SPA_ROOT / resource_path if resource_path else SPA_ROOT / "index.html"

    if candidate.is_file():
        # Decide content type from extension
        content_type, _ = mimetypes.guess_type(str(candidate))
        if not content_type:
            content_type = "application/octet-stream"
        return FileResponse(open(candidate, "rb"), content_type=content_type)

    # If not a real file, fall back to index.html (the SPA shell)
    index_path = SPA_ROOT / "index.html"
    if not index_path.is_file():
        raise Http404("SPA build not found")

    return FileResponse(open(index_path, "rb"), content_type="text/html")

def example_view(request):
    data = {"message": "Hello from Django"}
    return JsonResponse(data)

# def home(request):
#     # You can pass data to the template here
#     return render(request, "home.html")
# #
def gics_sector_list_api(request):
    data = [
        {
            "code": gs.code,
            "name": gs.name,
        }
        for gs in GICSSector.objects.all()
    ]
    return JsonResponse(data, safe=False)
#
# def kpi_list_api(request):
#     data = [
#         {
#             "id": k.id,
#             "name": k.name,
#             "unit": k.unit,
#             "direction": k.direction,
#         }
#         for k in KPI.objects.all()
#     ]
#     return JsonResponse(data, safe=False)