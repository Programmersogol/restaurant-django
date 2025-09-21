from django.db import models
from django.contrib.auth.models import User
from appshop.models import Product
# Create your models here.

class ShippingAddress(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    shipping_full_name= models.CharField(max_length=250)
    shipping_email= models.EmailField(max_length=200)
    shipping_phone=models.CharField(max_length=11,blank=True)
    shipping_address1 = models.CharField(max_length=250,blank=True)
    shipping_city=models.CharField(max_length=25,blank=True)
    shipping_state=models.CharField(max_length=25,blank=True)
    shipping_zipcode=models.CharField(max_length=25,blank=True)
    shipping_country=models.CharField(max_length=25,default='IRAN')
    shipping_old_cart=models.CharField(max_length=200,blank=True,null=True)


    class Meta:
        verbose_name_plural = 'Shipping Address'

    def __str__(self):
        return f'Shipping Address From {self.shipping_full_name}'
    

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'در انتظار پرداخت'),
        ('paid', 'پرداخت شده'),
        ('canceled', 'لغو شده'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=300)
    email = models.EmailField(max_length=300)
    shipping_address = models.TextField(max_length=150000)
    amount_paid = models.DecimalField(decimal_places=0, max_digits=12)
    date_order = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending') 

    def __str__(self):
        return f'Order- {self.id} '

    
class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,null=True)    
    products=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)    
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)    
    quantity=models.PositiveBigIntegerField(default=1)
    price=models.DecimalField(decimal_places=0,max_digits=12)

    def __str__(self):
        return f'Order Item - {str(self.id)}'