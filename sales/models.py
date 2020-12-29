from customers.models import Customer
from companies.models import Company
from products.models import Product
from c_cards.models import Card
from django.db import models
import uuid


class Sale(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, null=False, blank=False)
    id_company = models.ForeignKey(Company, on_delete=models.PROTECT, null=False, blank=False)
    id_customer = models.ForeignKey(Customer, on_delete=models.PROTECT, null=False, blank=False)
    id_card = models.ForeignKey(Card, on_delete=models.PROTECT, null=False, blank=False)
    products = models.ManyToManyField(Product)  # dar baixa no estoque
    sale_moment = models.DateTimeField(null=True, blank=True)
    send_moment = models.DateTimeField(null=True, blank=True)
    val = models.FloatField(null=False, blank=False)
    pay_moment = models.DateField(null=True, blank=True)  # para quitação
    pay_times = models.IntegerField(null=True, blank=True) # val (total) parcelado n vezes
    obs = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(null=False, blank=False, default=True)
    creation = models.DateTimeField(auto_now_add=True)