from companies.models import Company
from products.models import Product
from django.db import models
import uuid

class Buy(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, null=False, blank=False)
    id_company = models.ForeignKey(Company, on_delete=models.PROTECT, null=False, blank=False)
    id_product = models.ForeignKey(Product, on_delete=models.PROTECT, null=False, blank=False)  # dar entrada no estoque
    sale_moment = models.DateTimeField(null=True, blank=True)  # momento da compra
    send_moment = models.DateTimeField(null=True, blank=True)  # momento em que o produto foi recebido
    val = models.FloatField(null=False, blank=False)
    pay_moment = models.DateField(null=True, blank=True)  # para quitação
    pay_times = models.IntegerField(null=True, blank=True)  # val (total) parcelado n vezes
    obs = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(null=False, blank=False, default=True)
    creation = models.DateTimeField(auto_now_add=True)
