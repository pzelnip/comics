from django.db import models


class Comic(models.Model):
    issue_number = models.IntegerField(null=False)
