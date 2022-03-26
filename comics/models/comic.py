from decimal import Decimal
from django.db import models


CGC_GRADES = [
    (Decimal(grade), grade)
    for grade in (
        "0.5 1.0 1.5 1.8 2.0 2.5 3.0 3.5 4.0 4.5 5.0 5.5 6.0"
        " 6.5 7.0 7.5 8.0 8.5 9.0 9.2 9.4 9.6 9.8 9.9 10".split()
    )
]


class Series(models.Model):
    class Meta:
        verbose_name_plural = "Series"

    title = models.CharField(max_length=150, unique=True, null=False)
    slug = models.CharField(max_length=15, unique=True, null=False)

    def __str__(self):
        return self.title


class Comic(models.Model):
    series = models.ForeignKey(
        Series,
        on_delete=models.CASCADE,
        null=False,
        default=Series.objects.get(title="Unknown", slug="unkn").id,
    )
    issue_number = models.IntegerField(null=False, unique=True)
    year_released = models.IntegerField(blank=True, null=True)
    key_issue = models.BooleanField(default=False)
    notes = models.TextField(blank=True)
    # estimated_cost =

    def __str__(self):
        if self.series.slug != "xmen":
            return f"{self.series.title} #{self.issue_number}"

        label = f"X-Men #{self.issue_number}"
        if self.issue_number >= 139:
            label = f"Uncanny {label}"
        return label


class Copy(models.Model):
    class Meta:
        verbose_name_plural = "Copies"

    comic = models.ForeignKey(Comic, on_delete=models.CASCADE)
    slabbed = models.BooleanField(default=False)
    grade = models.DecimalField(
        max_digits=2, decimal_places=1, choices=CGC_GRADES, null=True, blank=True
    )
    notes = models.TextField(blank=True)
    # price_paid
