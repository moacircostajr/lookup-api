import uuid
import pytz
from django.db import models
from django.contrib.auth.models import AbstractUser
from companies.models import Company

#TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, null=False, blank=False)
    id_company = models.ForeignKey(Company, on_delete=models.PROTECT, null=True, blank=True)
    business_name = models.CharField(max_length=60, null=True, blank=False)
    cpf = models.CharField(max_length=11, null=True, blank=True)
    address = models.CharField(max_length=60, null=True, blank=False)
    complement = models.CharField(max_length=60, null=True, blank=True)
    neighborhood = models.CharField(max_length=60, null=True, blank=False)
    city = models.CharField(max_length=60, null=True, blank=False)
    state = models.CharField(max_length=60, null=True, blank=False)
    country = models.CharField(max_length=60, null=True, blank=False)
    zip_code = models.CharField(max_length=8, null=True, blank=False)
    phones = models.CharField(max_length=60, null=True, blank=True)
    # saiu time_zone, latitude e longitude
