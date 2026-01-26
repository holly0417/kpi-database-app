"""
URL configuration for kpi_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from kpi_app.views import spa_view

# kpi_project/urls.py = global entry router.
# kpi_app/urls.py = app‑specific routes, which are included into the project.
#kpi_project = global configurations for whole site
#kpi_app = self-contained app

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("kpi_app.urls")),
]

urlpatterns += [
    path("", spa_view, name="spa-root"),
]

# Catch-all SPA route (everything else not matched above)
urlpatterns += [
    re_path(
        r"^(?!api/|admin/)(?P<resource_path>.*)$",
        spa_view,
        name="spa-fallback",
    ),
]