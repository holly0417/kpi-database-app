from django.contrib import admin
from django.urls import path, re_path, include
from . import views
from .views import GICSLayersBySubIndustry, GicsSectorList, GicsIndustryGroupList, GicsIndustryList, GicsSubIndustryList, KPIList, KPIIndustryList, AllKPIsListedByName

urlpatterns = [
    path("kpis/", KPIList.as_view()),
    path("kpis/industry/", KPIIndustryList.as_view()),
    path("kpis/industry-list/", AllKPIsListedByName.as_view()),
    path("gics/", GicsSectorList.as_view()),
    path("gics/industry-groups/", GicsIndustryGroupList.as_view()),
    path("gics/industries/", GicsIndustryList.as_view()),
    path("gics/subindustries/", GicsSubIndustryList.as_view()),
    path("gics/get-layers-by-subindustry/", GICSLayersBySubIndustry.as_view()),
    # Any other Django URLs you explicitly want, e.g. auth, health checks, etc.
    # path("health/", health_view),
]