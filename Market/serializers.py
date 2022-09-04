from rest_framework import serializers
from Market.models import Store
from Market.models import Category
from Market.models import Cart
from Market.models import Items
from Market.models import Order
from User.models import Profile
from django.contrib.auth.models import User


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    # user= serializers.SlugRelatedField(queryset= User.objects.all(), slug_field='name') 
    user= serializers.ReadOnlyField(source= 'user.username')
    class Meta:
        model = Profile
        fields= ('url','pk', 'name', 'user', 'email', 'username', 'is_admin', 'created')

class StoreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Store
        fields=('url', 'pk', 'name', 'categories', 'items_sold', 'date')

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    stores= serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='store-detail')
    items= serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='items-detail')

    class Meta:
        model=Category
        fields=('url', 'pk', 'name', 'items', 'stores')

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    carts = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='cart-detail')
    item_category = serializers.SlugRelatedField(queryset= Category.objects.all(), slug_field='name') 

    class Meta:
        model= Items
        fields=('url', 'pk', 'name', 'price', 'carts', 'item_category', 'date')

class CartSerializer(serializers.HyperlinkedModelSerializer):
    owner= serializers.ReadOnlyField(source= 'owner.username')
    class Meta:
        model= Cart
        fields= ('url','pk', 'owner', 'items', 'total_price')

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    owner= serializers.ReadOnlyField(source= 'owner.username')
    class Meta:
        model= Order
        fields= ('url', 'pk','owner', 'items', 'total_price')
