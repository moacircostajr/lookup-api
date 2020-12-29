from companies.models import Company
from categories.models import Category
from django.db import models
import uuid


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, null=False, blank=False)
    id_company = models.ForeignKey(Company, on_delete=models.PROTECT, null=False, blank=True)
    id_category = models.ForeignKey(Category, on_delete=models.PROTECT, null=False, blank=True)
    description = models.CharField(max_length=60, null=False, blank=False)
    codebar = models.CharField(max_length=60, null=True, blank=True)
    ref = models.CharField(max_length=60, null=True, blank=True)
    un = models.CharField(max_length=10, null=False, blank=False)
    quant = models.FloatField(null=False, blank=False)
    val = models.FloatField(null=False, blank=False)
    detail = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(null=False, blank=False, default=True)
    creation = models.DateTimeField(auto_now_add=True)
