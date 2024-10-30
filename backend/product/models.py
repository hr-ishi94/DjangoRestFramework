from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(blank=True,null=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)

    @property
    def sale_price(self):
        return "%.2f"%(float(self.price)*0.8) 
    
    def other_amount(self):
        return 120