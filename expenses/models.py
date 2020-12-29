from categories.models import Category
from companies.models import Company
from django.db import models
import uuid


class Expense(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, null=False, blank=False)
    id_company = models.ForeignKey(Company, on_delete=models.PROTECT, null=False, blank=False)
    id_category = models.ForeignKey(Category, on_delete=models.PROTECT, null=False, blank=False)
    desc = models.CharField(max_length=60, null=False, blank=False)
    expense_moment = models.DateTimeField(null=True, blank=True)
    val = models.FloatField(null=False, blank=False)
    pay_moment = models.DateField(null=True, blank=True)  # para quitação
    pay_times = models.IntegerField(null=True, blank=True)
    obs = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(null=False, blank=False, default=True)
    creation = models.DateTimeField(auto_now_add=True)
