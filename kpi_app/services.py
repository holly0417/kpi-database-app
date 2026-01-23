from .models import Industry, KPI
from pathlib import Path

def create_industry(name, sector=None, code=None):
    industry, _ = Industry.objects.get_or_create(
        name=name,
        defaults={"sector": sector, "code": code},
    )
    return industry

def list_kpis_for_industry(industry_id):
    from .models import KPIIndustry
    return KPI.objects.filter(kpiindustry__industry_id=industry_id)

GICS = "~/PycharmProjects/testKPIDatabase/kpi_app/classifications/GICS CLEANED V1.xlsx"
ISIC = "~/PycharmProjects/testKPIDatabase/kpi_app/classifications/ISIC CLEANED V1.xlsx"

