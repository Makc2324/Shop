from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=30)
    picture = models.ImageField(upload_to='images/products/')
    description = models.TextField()
    price = models.FloatField()
    rating = models.FloatField()
    discount = models.FloatField(default=0)
    stock = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)

    
class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True )
    dilivery_address = models.CharField(max_length=500)
    product = models.ForeignKey(to=Product, on_delete=models.SET_NULL, null=True)

    

    
    


 
    

    
    

