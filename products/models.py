from django.db import models
from django.utils import timezone

# Create your models here.
class ProductModel(models.Model):
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Ürün'
        verbose_name_plural = 'Ürünler'

    productName = models.CharField(max_length=200,verbose_name="Ürün İsmi")
    quantity = models.IntegerField(verbose_name="Adet")
    price = models.BigIntegerField(verbose_name="Fiyat")
    recordTime = models.DateTimeField(default=timezone.now,verbose_name="Zaman")


    def __str__(self):
        return self.productName + "( " + str(self.quantity) + " )" 

