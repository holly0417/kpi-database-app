from rest_framework import serializers
from .models import KPI, KPIIndustry, Benchmark

class KPISerializer(serializers.ModelSerializer):
    class Meta:
        model = KPI
        fields = ["name", "description", "formula", "unit", "direction", "frequency"]