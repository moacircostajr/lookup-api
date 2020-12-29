from companies.models import Company
from django.db import models
import uuid


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, null=False, blank=False)
    id_company = models.ForeignKey(Company, on_delete=models.PROTECT, null=False, blank=True)
    desc = models.CharField(max_length=60, null=False, blank=False)
    is_product = models.BooleanField(null=False, blank=False, default=True)
    is_active = models.BooleanField(null=False, blank=False, default=True)
    creation = models.DateTimeField(auto_now_add=True)
