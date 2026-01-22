from django.db import models

# Create your models here.
# Persistence layer managed by Django ORM

class gics_sector(models.Model):
    code = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=200, unique=True)

class gics_industry_group(models.Model):
    code = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=200, unique=True)
    sector = models.ForeignKey(gics_sector, on_delete=models.CASCADE)

class gics_industry(models.Model):
    code = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=200, unique=True)
    industry_group = models.ForeignKey(gics_industry_group, on_delete=models.CASCADE)

class gics_sub_industry(models.Model):
    code = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=200, unique=True)
    industry = models.ForeignKey(gics_industry, on_delete=models.CASCADE)

class icb_industry(models.Model):
    code = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=200, unique=True)

class icb_super_sector(models.Model):
    code = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=200, unique=True)
    industry = models.ForeignKey(icb_industry, on_delete=models.CASCADE)

class icb_sector(models.Model):
    code = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=200, unique=True)
    super_sector = models.ForeignKey(icb_super_sector, on_delete=models.CASCADE)


class icb_sub_sector(models.Model):
    code = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=200, unique=True)
    sector = models.ForeignKey(icb_sector, on_delete=models.CASCADE)


class Industry(models.Model):
    name = models.CharField(max_length=200, unique=True)
    gics_sub_industry = models.ForeignKey(
        gics_sub_industry,
        null=True, blank=True,
        on_delete=models.SET_NULL,
    )
    icb_sub_sector = models.ForeignKey(
        icb_sub_sector,
        null=True, blank=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return self.name

class KPI(models.Model):
    DIRECTION_CHOICES = [
        ("up", "Higher is better"),
        ("down", "Lower is better"),
        ("target", "Closer to target is better"),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    formula = models.TextField(blank=True, null=True)
    unit = models.CharField(max_length=50, blank=True, null=True)
    direction = models.CharField(
        max_length=10, choices=DIRECTION_CHOICES, blank=True, null=True
    )
    frequency = models.CharField(max_length=50, blank=True, null=True)

class KPIIndustry(models.Model):
    kpi = models.ForeignKey(KPI, on_delete=models.CASCADE)
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)
    relevance = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        unique_together = ("kpi", "industry")


class Benchmark(models.Model):
    kpi = models.ForeignKey(KPI, on_delete=models.CASCADE)
    industry = models.ForeignKey(Industry, null=True, blank=True, on_delete=models.SET_NULL)
    geography = models.CharField(max_length=100, blank=True, null=True)
    company_size = models.CharField(max_length=100, blank=True, null=True)
    period = models.CharField(max_length=50, blank=True, null=True)
    value_type = models.CharField(max_length=50, blank=True, null=True)
    value_low = models.FloatField(blank=True, null=True)
    value_high = models.FloatField(blank=True, null=True)
    source = models.URLField(blank=True, null=True)