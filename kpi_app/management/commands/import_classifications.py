from django.core.management.base import BaseCommand
import pandas as pd
from kpi_app.models import GICSSector, GICSIndustryGroup, GICSIndustry, GICSSubIndustry
import numpy as np
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
GICS = BASE_DIR / "kpi_app" / "classifications" / "GICS CLEANED V1.xlsx"

# excel column: model column
sector_column_map = {
    "SECTOR CODE": "code",
    "SECTOR": "name"
}

industry_group_column_map = {
    "INDUSTRY GROUP CODE": "code",
    "INDUSTRY GROUP": "name",
    "SECTOR CODE": "sector"
}

industry_column_map = {
    "INDUSTRY CODE": "code",
    "INDUSTRY": "name",
    "INDUSTRY GROUP CODE": "industry_group"
}

sub_industry_column_map = {
    "SUBINDUSTRY CODE": "code",
    "SUBINDUSTRY": "name",
    "INDUSTRY CODE": "industry"
}
class Command(BaseCommand):
    help = "Populate database with GICS classifications"

    def handle(self, *args, **options):
        gics_xls = pd.ExcelFile(GICS)
        print(gics_xls.sheet_names)

        gics_sector_df = pd.read_excel(GICS, sheet_name="SECTOR")   # or sheet index, e.g. 0
        gics_sector_df = gics_sector_df.replace({np.nan: None})
        gics_sector_df = gics_sector_df.rename(columns=sector_column_map)

        #read_excel already skips first row for us
        for _, row in gics_sector_df.iterrows():
            if pd.isna(row["code"]) or pd.isna(row["name"]):
                continue

            GICSSector.objects.update_or_create(
                code=str(int(float(row["code"]))),
                defaults={
                    "name": row["name"],
                },
            )

        gics_industry_group_df = pd.read_excel(GICS, sheet_name="INDUSTRYGROUP")
        gics_industry_group_df = gics_industry_group_df.replace({np.nan: None})
        gics_industry_group_df = gics_industry_group_df.rename(columns=industry_group_column_map)

        for _, row in gics_industry_group_df.iterrows():
            if pd.isna(row["code"]) or pd.isna(row["name"]):
                continue

            if pd.isna(row["sector"]):
                continue

            sector = GICSSector.objects.get(code=str(row["sector"]))

            GICSIndustryGroup.objects.update_or_create(
                code=str(int(float(row["code"]))),
                defaults={
                    "name": row["name"],
                    "sector": sector
                },
            )

        gics_industry_df = pd.read_excel(GICS, sheet_name="INDUSTRY")
        gics_industry_df = gics_industry_df.replace({np.nan: None})
        gics_industry_df = gics_industry_df.rename(columns=industry_column_map)

        for _, row in gics_industry_df.iterrows():
            if pd.isna(row["code"]) or pd.isna(row["name"]):
                continue

            if pd.isna(row["industry_group"]):
                continue

            industry_group = GICSIndustryGroup.objects.get(code=str(row["industry_group"]))

            GICSIndustry.objects.update_or_create(
                code=str(int(float(row["code"]))),
                defaults={
                    "name": row["name"],
                    "industry_group": industry_group
                },
            )

        gics_sub_industry_df = pd.read_excel(GICS, sheet_name="SUBINDUSTRY")
        gics_sub_industry_df = gics_sub_industry_df.replace({np.nan: None})
        gics_sub_industry_df = gics_sub_industry_df.rename(columns=sub_industry_column_map)

        for _, row in gics_sub_industry_df.iterrows():
            if pd.isna(row["code"]) or pd.isna(row["name"]):
                continue

            if pd.isna(row["industry"]):
                continue

            industry = GICSIndustry.objects.get(code=str(row["industry"]))

            GICSSubIndustry.objects.update_or_create(
                code=str(int(float(row["code"]))),
                defaults={
                    "name": row["name"],
                    "industry": industry
                },
            )

        si = GICSSubIndustry.objects.get(code="10101020")
        print(
            si.industry.industry_group.sector.name,
            "→",
            si.industry.industry_group.name,
            "→",
            si.industry.name,
            "→",
            si.name,
        )

