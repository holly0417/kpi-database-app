from rest_framework import serializers
from kpi_app.models import KPI, KPIIndustry, Benchmark, GICSSector, GICSIndustryGroup, GICSIndustry, GICSSubIndustry

#here we explicitly define which fields we want to have in the API output

class GICSSectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = GICSSector
        fields = ["id", "code", "name"]

class GICSIndustryGroupSerializer(serializers.ModelSerializer):
    sector = serializers.PrimaryKeyRelatedField(
        queryset=GICSSector.objects.all()
    )
    class Meta:
        model = GICSIndustryGroup
        fields = ["id", "code", "name", "sector"]

class GICSIndustrySerializer(serializers.ModelSerializer):
    industry_group = serializers.PrimaryKeyRelatedField(
        queryset=GICSIndustryGroup.objects.all()
    )
    class Meta:
        model = GICSIndustry
        fields = ["id", "code", "name", "industry_group"]

class GICSSubIndustrySerializer(serializers.ModelSerializer):
    industry = serializers.PrimaryKeyRelatedField(
        queryset=GICSIndustry.objects.all()
    )
    class Meta:
        model = GICSSubIndustry
        fields = ["id", "code", "name", "industry"]

class KPISerializer(serializers.ModelSerializer):
    class Meta:
        model = KPI
        fields = ["id", "name", "description", "formula", "unit", "direction", "frequency"]

class KPIIndustrySerializer(serializers.ModelSerializer):
    kpi = serializers.PrimaryKeyRelatedField(
        queryset=KPI.objects.all()
    )
    sector = serializers.PrimaryKeyRelatedField(
        queryset=GICSSector.objects.all()
    )
    industry_group = serializers.PrimaryKeyRelatedField(
        queryset=GICSIndustryGroup.objects.all()
    )
    industry = serializers.PrimaryKeyRelatedField(
        queryset=GICSIndustry.objects.all()
    )
    sub_industry = serializers.PrimaryKeyRelatedField(
        queryset=GICSSubIndustry.objects.all()
    )

    class Meta:
        model = KPIIndustry
        fields = ["id", "kpi", "sector", "industry_group", "industry", "sub_industry"]


class BenchmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benchmark
        fields = [
            "id",
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