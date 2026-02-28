from typing import Any

from kpi_app.models import KPI, GICSSector, GICSIndustryGroup, GICSIndustry, GICSSubIndustry, KPIIndustry


def list_all_kpis():
    data = [
        {
            "id": k.id,
            "name": k.name,
            "description": k.description,
            "formula": k.formula,
            "unit": k.unit,
            "direction": k.direction,
            "frequency": k.frequency
        }
        for k in KPI.objects.all()
    ]

    return data

def list_all_kpis_industry():
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
        for k in KPIIndustry.objects.all()
    ]

    return data

def list_kpis_for_industry(industry_id):
    return KPI.objects.filter(kpiindustry__industry_id=industry_id)


def find_all_sectors():
    data = [
        {
            "id": k.id,
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
            "id": k.id,
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
            "id": k.id,
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
            "id": k.id,
            "code": k.code,
            "name": k.name,
        }
        for k in raw_data
    ]
    return data

def get_all_GICS_layers_by_subindustry(subindustry_code: str):
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

