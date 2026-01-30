from django.contrib import admin
from django.urls import path, re_path, include
from . import views
from .views import spa_view, GicsSectorList, GicsIndustryGroupList, GicsIndustryList, GicsSubIndustryList

urlpatterns = [

    # path("api/kpis/", views.kpi_list_api, name="kpi_list_api"),
    path("gics/", GicsSectorList.as_view()),
    path("gics/industry-groups/", GicsIndustryGroupList.as_view()),
    path("gics/industries/", GicsIndustryList.as_view()),
    path("gics/subindustries/", GicsSubIndustryList.as_view()),
    # Any other Django URLs you explicitly want, e.g. auth, health checks, etc.
    # path("health/", health_view),

]