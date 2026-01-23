from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("api/kpis/", views.kpi_list_api, name="kpi_list_api"),
    path("api/gics/", views.gics_sector_list_api, name="gics_sector_list_api"),
]