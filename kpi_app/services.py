from typing import Any
from django.http import Http404

from kpi_app.models import KPI, GICSSector, GICSIndustryGroup, GICSIndustry, GICSSubIndustry, KPIIndustry
from .serializers import (KPISerializer, KPIIndustrySerializer,
                          GICSSectorSerializer, GICSIndustryGroupSerializer,
                          GICSIndustrySerializer, GICSSubIndustrySerializer)

def list_all_sectors():
    data = GICSSector.objects.all()
    serializer = GICSSectorSerializer(data, many=True)
    return serializer.data


def list_all_kpis_industry():
    listOfKPIs = KPIIndustry.objects.select_related('kpi', 'sector', 'industry_group', 'industry', 'sub_industry').all()

    data = [
        {
            "id": k.id,
            "name": k.kpi.name,
            "description": k.kpi.description,
            "formula": k.kpi.formula,
            "unit": k.kpi.unit,
            "direction": k.kpi.direction,
            "frequency": k.kpi.frequency,
            "sector": k.sector.name,
            "industry_group": k.industry_group.name,
            "industry": k.industry.name,
            "sub_industry": k.sub_industry.name,
        }
        for k in listOfKPIs
    ]

    return data

def list_kpis_for_industry(industry_id):
    return KPI.objects.filter(kpiindustry__industry_id=industry_id)

def find_industry_group(sector_code: str) -> list[dict[str, Any]]:
    raw_data = GICSIndustryGroup.objects.filter(sector__code=sector_code)
    serializer = GICSIndustryGroupSerializer(raw_data, many=True)
    return serializer.data


def find_industry(industry_group_code: str) -> list[dict[str, Any]]:
    raw_data = GICSIndustry.objects.filter(industry_group__code=industry_group_code)
    serializer = GICSIndustrySerializer(raw_data, many=True)
    return serializer.data


def find_subindustry(industry_code: str) -> list[str]:
    raw_data = GICSSubIndustry.objects.filter(industry__code=industry_code)
    serializer = GICSSubIndustrySerializer(raw_data, many=True)
    return serializer.data

def get_all_GICS_layers_by_subindustry(subindustry_code: str):
    try:
        chosen_subindustry = GICSSubIndustry.objects.get(code=subindustry_code)
        industry = chosen_subindustry.industry
        industry_group = industry.industry_group
        sector = industry_group.sector

        data = {
            "sector": {
                "id": sector.id,
                "code": sector.code,
                "name": sector.name
            },
            "industry_group": {
                "id": industry_group.id,
                "code": industry_group.code,
                "name": industry_group.name
            },
            "industry": {
                "id": industry.id,
                "code": industry.code,
                "name": industry.name
            },
            "sub_industry": {
                "id": chosen_subindustry.id,
                "code": chosen_subindustry.code,
                "name": chosen_subindustry.name
            }
        }
        return data
    except GICSSubIndustry.DoesNotExist:
        raise Http404("subindustry not found")


