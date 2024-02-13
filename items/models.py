from django.db import models

class Item(models.Model):
    sku = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    tags = models.TextField()  
    stock_status = models.CharField(max_length=50)
    in_stock = models.IntegerField(default=0)
    available_stock = models.IntegerField()

    def __str__(self):
        return self.name
