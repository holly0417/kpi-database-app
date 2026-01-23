from django.db import models


# Create your models here.
# Persistence layer managed by Django ORM

class GICSSector(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.code} - {self.name}"


class GICSIndustryGroup(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=200)
    sector = models.ForeignKey(GICSSector,
                                    on_delete=models.PROTECT,
                                    related_name="industry_groups")

    def __str__(self):
        return f"{self.code} - {self.name}"


class GICSIndustry(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=200)
    industry_group = models.ForeignKey(GICSIndustryGroup,
                                            on_delete=models.PROTECT,
                                            related_name="industries")

    def __str__(self):
        return f"{self.code} - {self.name}"


class GICSSubIndustry(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=200)
    industry = models.ForeignKey(GICSIndustry,
                                      on_delete=models.PROTECT,
                                      related_name="subindustries")

    def __str__(self):
        return f"{self.code} - {self.name}"


class ISICSector(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.code} - {self.name}"


class ISICIndustryGroup(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=200)
    sector = models.ForeignKey(ISICSector,
                                    on_delete=models.PROTECT,
                                    related_name="industry_groups")

    def __str__(self):
        return f"{self.code} - {self.name}"


class ISICIndustry(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=200)
    industry_group = models.ForeignKey(ISICIndustryGroup,
                                            on_delete=models.PROTECT,
                                            related_name="industries")

    def __str__(self):
        return f"{self.code} - {self.name}"


class ISICSubIndustry(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=200)
    industry = models.ForeignKey(ISICIndustry,
                                      on_delete=models.PROTECT,
                                      related_name="subindustries")

    def __str__(self):
        return f"{self.code} - {self.name}"


class Sector(models.Model):
    name = models.CharField(max_length=200, unique=True)
    gics_sector = models.ForeignKey(
        GICSSector,
        null=True, blank=True,
        on_delete=models.SET_NULL,
    )
    isic_sector = models.ForeignKey(
        ISICSector,
        null=True, blank=True,
        on_delete=models.SET_NULL,
    )

    # this allows us to print the name instead of the generic object rep. in memory
    # <MyClass object at 0x...>
    def __str__(self):
        return self.name


class IndustryGroup(models.Model):
    name = models.CharField(max_length=200, unique=True)
    gics_industry_group = models.ForeignKey(
        GICSIndustryGroup,
        null=True, blank=True,
        on_delete=models.SET_NULL,
    )
    isic_industry_group = models.ForeignKey(
        ISICIndustryGroup,
        null=True, blank=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return self.name


class Industry(models.Model):
    name = models.CharField(max_length=200, unique=True)
    gics_industry = models.ForeignKey(
        GICSIndustry,
        null=True, blank=True,
        on_delete=models.SET_NULL,
    )
    isic_industry = models.ForeignKey(
        ISICIndustry,
        null=True, blank=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return self.name


class Subindustry(models.Model):
    name = models.CharField(max_length=200, unique=True)
    gics_sub_industry = models.ForeignKey(
        GICSSubIndustry,
        null=True, blank=True,
        on_delete=models.SET_NULL,
    )
    isic_sub_industry = models.ForeignKey(
        ISICSubIndustry,
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
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    industry_group = models.ForeignKey(IndustryGroup, on_delete=models.CASCADE)
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)
    sub_industry = models.ForeignKey(Subindustry, on_delete=models.CASCADE)
    relevance = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        unique_together = ("kpi", "sub_industry")


class Benchmark(models.Model):
    kpi = models.ForeignKey(KPI, on_delete=models.CASCADE)
    sector = models.ForeignKey(Sector, null=True, blank=True, on_delete=models.SET_NULL)
    industry_group = models.ForeignKey(IndustryGroup, null=True, blank=True, on_delete=models.SET_NULL)
    industry = models.ForeignKey(Industry, null=True, blank=True, on_delete=models.SET_NULL)
    sub_industry = models.ForeignKey(Subindustry, null=True, blank=True, on_delete=models.SET_NULL)
    geography = models.CharField(max_length=100, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    period = models.CharField(max_length=50, blank=True, null=True)
    value_type = models.CharField(max_length=50, blank=True, null=True)
    value_low = models.FloatField(blank=True, null=True)
    value_high = models.FloatField(blank=True, null=True)
    source = models.URLField(blank=True, null=True)
