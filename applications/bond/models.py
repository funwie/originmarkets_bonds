from django.db import models
import pycountry

CURRENCY_CODES = [currency.alpha_3 for currency in pycountry.currencies]


class LegalEntity(models.Model):
    lei = models.CharField(primary_key=True, max_length=20)
    legal_name = models.CharField(max_length=255)
    legal_address = models.CharField(max_length=255, blank=True)
    legal_jurisdiction = models.CharField(max_length=2, blank=True)
    status = models.CharField(max_length=100, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']


class Bond(models.Model):
    isin = models.CharField(primary_key=True, max_length=12)
    size = models.BigIntegerField()
    currency = models.CharField(max_length=3)
    maturity = models.DateField()
    lei = models.CharField(max_length=20)
    owner = models.ForeignKey('auth.User', related_name='bonds', on_delete=models.RESTRICT)
    legal_entity = models.ForeignKey(LegalEntity, related_name='legal_entity', on_delete=models.SET_NULL, blank=True, null=True)
    legal_name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']