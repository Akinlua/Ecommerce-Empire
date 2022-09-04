from django.db import models
from User.models import Profile
# Create your models here.

class Store(models.Model):
    name=models.CharField(max_length=250, unique=True)
    date=models.DateTimeField(auto_now_add=True)
    categories= models.ManyToManyField('Category', related_name='stores')
    items_sold= models.IntegerField()
    def __str__(self):
        return self.name

class Category(models.Model):
    name= models.CharField(max_length=250, unique=True)

    class Meta:
        ordering=['name']

    def __str__(self):
        return self.name

class Items(models.Model):
    name= models.CharField(max_length=250, unique=True)
    price=models.IntegerField()
    item_category= models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# cart: goods that you want to keep for later
class Cart(models.Model):
    owner= models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    items= models.ManyToManyField(Items, related_name='carts')
    total_price= models.IntegerField()
    
# order:goods that you want to buy now.
class Order(models.Model):
    owner= models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    items= models.ManyToManyField(Items, related_name='order')
    total_price= models.IntegerField()

