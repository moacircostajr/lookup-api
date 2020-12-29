from companies.models import Company
from django.db import models
import uuid


class Card(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, null=False, blank=False)
    id_company = models.ForeignKey(Company, on_delete=models.PROTECT, null=False, blank=False)
    card_name = models.CharField(max_length=60, null=True, blank=False)
    pay_day = models.CharField(max_length=60, null=False, blank=False)  # dia em que o cartão irá creditar o valor das vendas
    swear = models.CharField(max_length=60, null=False, blank=False)  # juros
    is_active = models.BooleanField(null=False, blank=False, default=True)
    creation = models.DateTimeField(auto_now_add=True)
