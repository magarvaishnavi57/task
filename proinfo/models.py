from django.db import models

class Product(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField()
    cost_per_item=models.IntegerField(default=0)
    stock_quantity=models.IntegerField(default=0)
    volume=models.IntegerField(default=0)

    def save(self,*args,**kwargs):
        self.volume= self.cost_per_item * self.stock_quantity
        super(Product, self).save(*args,**kwargs)

    def __str__(self):
        return self.name

# Create your models here.
