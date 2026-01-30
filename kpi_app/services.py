from typing import List, Dict, Any

from django.http import JsonResponse

from .models import Industry, KPI, GICSSector, GICSIndustryGroup, GICSIndustry, GICSSubIndustry
from pathlib import Path
from .serializers import GICSSectorSerializer


def create_industry(name, sector=None, code=None):
    industry, _ = Industry.objects.get_or_create(
        name=name,
        defaults={"sector": sector, "code": code},
    )
    return industry


def find_all_sectors():
    data = [
        {
            "code": k.code,
            "name": k.name,
        }
        for k in GICSSector.objects.all()
    ]

    return data


def find_industry_group(sector_code: str) -> list[dict[str, Any]]:
    raw_data = GICSIndustryGroup.objects.filter(sector__code=sector_code)

    data = [
        {
            "code": k.code,
            "name": k.name,
        }
        for k in raw_data
    ]

    return data


def find_industry(industry_group_code: str) -> list[dict[str, Any]]:
    raw_data = GICSIndustry.objects.filter(industry_group__code=industry_group_code)
    data = [
        {
            "code": k.code,
            "name": k.name,
        }
        for k in raw_data
    ]
    return data


def find_subindustry(industry_code: str) -> list[str]:
    raw_data = GICSSubIndustry.objects.filter(industry__code=industry_code)
    data = [
        {
            "code": k.code,
            "name": k.name,
        }
        for k in raw_data
    ]
    return data


def list_kpis_for_industry(industry_id):
    from .models import KPIIndustry
    return KPI.objects.filter(kpiindustry__industry_id=industry_id)


GICS = "~/PycharmProjects/testKPIDatabase/kpi_app/classifications/GICS CLEANED V1.xlsx"
ISIC = "~/PycharmProjects/testKPIDatabase/kpi_app/classifications/ISIC CLEANED V1.xlsx"
