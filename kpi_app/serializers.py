from rest_framework import serializers
from .models import Industry, KPI, GICSSector, GICSIndustryGroup, GICSIndustry, GICSSubIndustry

class GICSSectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = GICSSector
        fields = ['code', 'name']

class GICSIndustryGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = GICSIndustryGroup
        fields = ['code', 'name', 'sector']

class GICSIndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = GICSIndustry
        fields = ['code', 'name', 'industry_group']

class GICSSubIndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = GICSSubIndustry
        fields = ['code', 'name', 'industry']