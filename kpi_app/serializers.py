from rest_framework import serializers
from .models import KPI, KPIIndustry, Benchmark

class KPISerializer(serializers.ModelSerializer):
    class Meta:
        model = KPI
        fields = ["name", "description", "formula", "unit", "direction", "frequency"]

class KPIIndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = KPIIndustry
        fields = ["kpi", "sector", "industry_group", "industry", "sub_industry", "relevance"]


class BenchmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benchmark
        fields = [
            "kpi",
            "sector",
            "industry_group",
            "industry",
            "sub_industry",
            "geography",
            "company",
            "period",
            "value_type",
            "value_low",
            "value_high",
            "source"
            ]