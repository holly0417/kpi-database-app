from django.core.management.base import BaseCommand
import pandas as pd
from kpi_app import services
from kpi_app.models import GICSSector, GICSIndustryGroup, GICSIndustry, GICSSubIndustry, ISICSector, ISICIndustryGroup, ISICIndustry, ISICSubIndustry
import numpy as np

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
    help = "Populate database with GICS + ISIC classifications"

    def handle(self, *args, **options):
        gics_xls = pd.ExcelFile(services.GICS)
        print(gics_xls.sheet_names)

        gics_sector_df = pd.read_excel(services.GICS, sheet_name="SECTOR")   # or sheet index, e.g. 0
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

        gics_industry_group_df = pd.read_excel(services.GICS, sheet_name="INDUSTRYGROUP")
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

        gics_industry_df = pd.read_excel(services.GICS, sheet_name="INDUSTRY")
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

        gics_sub_industry_df = pd.read_excel(services.GICS, sheet_name="SUBINDUSTRY")
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

        isic_sector_df = pd.read_excel(services.ISIC, sheet_name="SECTOR")
        isic_sector_df = isic_sector_df.replace({np.nan: None})
        isic_sector_df = isic_sector_df.rename(columns=sector_column_map)

        for _, row in isic_sector_df.iterrows():
            if pd.isna(row["code"]) or pd.isna(row["name"]):
                continue

            ISICSector.objects.update_or_create(
                code=str(row["code"]).strip(),
                defaults={
                    "name": row["name"],
                },
            )

        isic_industry_group_df = pd.read_excel(services.ISIC, sheet_name="INDUSTRYGROUP")
        isic_industry_group_df = isic_industry_group_df.replace({np.nan: None})
        isic_industry_group_df = isic_industry_group_df.rename(columns=industry_group_column_map)

        for _, row in isic_industry_group_df.iterrows():
            if pd.isna(row["code"]) or pd.isna(row["name"]):
                continue

            if pd.isna(row["sector"]):
                continue

            sector = ISICSector.objects.get(code=row["sector"])

            ISICIndustryGroup.objects.update_or_create(
                code=str(int(float(row["code"]))),
                defaults={
                    "name": row["name"],
                    "sector": sector
                },
            )

        isic_industry_df = pd.read_excel(services.ISIC, sheet_name="INDUSTRY")
        isic_industry_df = isic_industry_df.replace({np.nan: None})
        isic_industry_df = isic_industry_df.rename(columns=industry_column_map)

        for _, row in isic_industry_df.iterrows():
            if pd.isna(row["code"]) or pd.isna(row["name"]):
                continue

            if pd.isna(row["industry_group"]):
                continue

            industry_group = ISICIndustryGroup.objects.get(code=str(row["industry_group"]))

            ISICIndustry.objects.update_or_create(
                code=str(int(float(row["code"]))),
                defaults={
                    "name": row["name"],
                    "industry_group": industry_group
                },
            )

        isic_subindustry_df = pd.read_excel(services.ISIC, sheet_name="SUBINDUSTRY")
        isic_subindustry_df = isic_subindustry_df.replace({np.nan: None})
        isic_subindustry_df = isic_subindustry_df.rename(columns=sub_industry_column_map)

        for _, row in isic_subindustry_df.iterrows():
            if pd.isna(row["code"]) or pd.isna(row["name"]):
                continue

            if pd.isna(row["industry"]):
                continue

            industry = ISICIndustry.objects.get(code=str(row["industry"]))

            ISICSubIndustry.objects.update_or_create(
                code=str(int(float(row["code"]))),
                defaults={
                    "name": row["name"],
                    "industry": industry
                },
            )

        example_ind = ISICSubIndustry.objects.get(code="0116")
        print(
            example_ind.industry.industry_group.sector.name,
            "→",
            example_ind.industry.industry_group.name,
            "→",
            example_ind.industry.name,
            "→",
            example_ind.name,
        )