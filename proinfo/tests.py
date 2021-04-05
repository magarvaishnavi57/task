from django.test import TestCase
from .models import Product

class ProductTestcase(TestCase):
    def test_volume(self):
        p=Product.objects.create(name=' TV Remote',description='quality is very good',cost_per_item=80,stock_quantity=200)
        self.assertEqual(p.volume,(p.cost_per_item*p.stock_quantity))

    def test_zerovolume(self):
        p = Product.objects.create(name=' TV Remote', description='quality is very good', cost_per_item=80,
                                   stock_quantity=0)
        self.assertEqual(p.volume,0)
