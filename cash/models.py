from companies.models import Company
from django.db import models
import uuid


class Cash(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, null=False, blank=False)
    id_company = models.ForeignKey(Company, on_delete=models.PROTECT, null=False, blank=False)
    day = models.DateField(null=False, blank=False)
    income = models.FloatField(null=False, blank=False)
    expense = models.FloatField(null=False, blank=False)
    cash = models.FloatField(null=False, blank=False)
    accumulated = models.FloatField(null=False, blank=False)
    is_active = models.BooleanField(null=False, blank=False, default=True)
    creation = models.DateTimeField(auto_now_add=True)
