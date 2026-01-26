from django.contrib import admin
from django.urls import path, re_path, include
from . import views
from .views import spa_view

urlpatterns = [

    # path("api/kpis/", views.kpi_list_api, name="kpi_list_api"),
    path("gics/", views.gics_sector_list_api, name="gics_sector_list_api"),
    path("example/", views.example_view, name="example"),

    # Any other Django URLs you explicitly want, e.g. auth, health checks, etc.
    # path("health/", health_view),


]