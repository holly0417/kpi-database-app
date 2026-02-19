import mimetypes

from django.http import JsonResponse, Http404, HttpResponse, FileResponse
from django.conf import settings
from pathlib import Path

from rest_framework import status
from rest_framework.views import APIView

from .models import Industry, KPI, KPIIndustry, Benchmark, GICSSector, GICSIndustryGroup, GICSIndustry, GICSSubIndustry

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services import find_all_sectors, find_industry_group, find_industry, find_subindustry, list_all_kpis, list_kpis_for_industry
from .serializers import KPISerializer, KPIIndustrySerializer, BenchmarkSerializer

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


# def home(request):
#     # You can pass data to the template here
#     return render(request, "home.html")
# #
class GicsSectorList(APIView):
    def get(self, request):
        data = find_all_sectors()
        return JsonResponse(data, safe=False)

class GicsIndustryGroupList(APIView):
    def get(self, request, *args, **kwargs):
        sector_code = request.query_params.get("sector_code")  # same as GET
        data = find_industry_group(str(sector_code))
        return JsonResponse(data, safe=False)

class GicsIndustryList(APIView):
    def get(self, request, *args, **kwargs):
        industry_group_code = request.query_params.get("industry_group_code")  # same as GET
        data = find_industry(str(industry_group_code))
        return JsonResponse(data, safe=False)

class GicsSubIndustryList(APIView):
    def get(self, request, *args, **kwargs):
        industry_code = request.query_params.get("industry_code")  # same as GET
        data = find_subindustry(str(industry_code))
        return JsonResponse(data, safe=False)

class KPIList(APIView):
    def get(self, request, *args, **kwargs):
        kpis = KPI.objects.all()
        serializer = KPISerializer(kpis, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = KPISerializer(data=request.data)
        if serializer.is_valid():
            kpi = serializer.save()
            return Response(KPISerializer(kpi).data, status=status.HTTP_201_CREATED)
        print("SERIALIZER ERRORS:", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class KPIIndustryList(APIView):
#     def get(self, request):
#         kpi_industry = KPIIndustry.objects.all()
#         serializer = KPIIndustrySerializer(kpi_industry, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = KPISerializer(data=request.data)
#         if serializer.is_valid():
#             kpi = serializer.save()
#             return Response(KPISerializer(kpi).data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



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
