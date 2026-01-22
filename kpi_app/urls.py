from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("api/kpis/", views.kpi_list_api, name="kpi_list_api"),
]