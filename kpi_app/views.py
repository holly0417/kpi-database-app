import mimetypes
import logging
from django.http import JsonResponse, Http404, FileResponse
from django.conf import settings
from pathlib import Path

from rest_framework import status
from rest_framework.views import APIView

from kpi_app.models import KPI, KPIIndustry, GICSSector, GICSIndustryGroup, GICSIndustry, GICSSubIndustry

from rest_framework.response import Response
from .services import list_all_sectors, find_industry_group, find_industry, find_subindustry, get_all_GICS_layers_by_subindustry, list_all_kpis_industry
from .serializers import KPISerializer, KPIIndustrySerializer, GICSSectorSerializer

# Create your views here.
SPA_ROOT = Path(settings.BASE_DIR) / "frontend" / "dist" / "spa"
logger = logging.getLogger(__name__)


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
        return FileResponse(candidate.open("rb"), content_type=content_type)

    # If not a real file, fall back to index.html (the SPA shell)
    index_path = SPA_ROOT / "index.html"
    if not index_path.is_file():
        raise Http404("SPA build not found")

    return FileResponse(index_path.open("rb"), content_type="text/html")


# def home(request):
#     # You can pass data to the template here
#     return render(request, "home.html")
# #
class GicsSectorList(APIView):
    def get(self, request):
        return Response(list_all_sectors())

class GicsIndustryGroupList(APIView):
    def get(self, request, *args, **kwargs):
        sector_code = request.query_params.get("sector_code")  # same as GET
        if not sector_code:
            return Response({"error": "sector_code is required"}, status=400)
        data = find_industry_group(str(sector_code))
        return Response(data)

class GicsIndustryList(APIView):
    def get(self, request, *args, **kwargs):
        industry_group_code = request.query_params.get("industry_group_code")  # same as GET
        if not industry_group_code:
            return Response({"error": "industry_group_code is required"}, status=400)
        data = find_industry(str(industry_group_code))
        return Response(data)

class GicsSubIndustryList(APIView):
    def get(self, request, *args, **kwargs):
        industry_code = request.query_params.get("industry_code")  # same as GET
        if not industry_code:
            return Response({"error": "industry_code is required"}, status=400)
        data = find_subindustry(str(industry_code))
        return Response(data)

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

        logger.warning("Serializer validation failed: %s", serializer.errors)
        print("SERIALIZER ERRORS:", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class KPIIndustryList(APIView):
    def get(self, request, *args, **kwargs):
        kpiIndustry = KPIIndustry.objects.all()
        serializer = KPIIndustrySerializer(kpiIndustry, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = KPIIndustrySerializer(data=request.data)
        if serializer.is_valid():
            kpi_industry = serializer.save()
            return Response(KPIIndustrySerializer(kpi_industry).data, status=status.HTTP_201_CREATED)
        logger.warning("Serializer validation failed: %s", serializer.errors)
        print("SERIALIZER ERRORS:", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GICSLayersBySubIndustry(APIView):
    def get(self, request, *args, **kwargs):
        sub_industry_code = request.query_params.get("sub_industry_code")
        if not sub_industry_code:
            return Response({"error": "sub_industry_code is required"}, status=400)
        data = get_all_GICS_layers_by_subindustry(str(sub_industry_code))
        return Response(data)

class AllKPIsListedByName(APIView):
    def get(self, request, *args, **kwargs):
        data = list_all_kpis_industry()
        return Response(data)

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
