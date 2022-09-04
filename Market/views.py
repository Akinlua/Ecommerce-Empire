from Market.models import Store
from Market.models import Category
from Market.models import Cart
from Market.models import Items
from Market.models import Order
from Market.serializers import StoreSerializer
from Market.serializers import CategorySerializer
from Market.serializers import CartSerializer
from Market.serializers import ItemSerializer
from Market.serializers import OrderSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.shortcuts import render
from django_filters import rest_framework as filters
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter, FilterSet
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.throttling import ScopedRateThrottle
from Market import custompermission
from User.views import ProfileDetail, ProfileList

class Storelist(generics.ListCreateAPIView):
    queryset= Store.objects.all()
    serializer_class= StoreSerializer
    name= 'store-list'
    search_fields= ['name', 'categories']

class StoreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset= Store.objects.all()
    serializer_class= StoreSerializer
    name= 'store-detail'

class Categorylist(generics.ListCreateAPIView):
    queryset= Category.objects.all()
    serializer_class= CategorySerializer
    name= 'category-list'
    

class Categorydetail(generics.RetrieveUpdateDestroyAPIView):
    queryset= Category.objects.all()
    serializer_class= CategorySerializer
    name= 'category-detail'

class CartList(generics.ListCreateAPIView):
    queryset=Cart.objects.all()
    serializer_class= CartSerializer
    name= 'cart-list'
    search_fields= ['items', 'total_price', ]
   
    def perform_create(self, serializer): 
        serializer.save(owner=self.request.user.profile)
    
    
class CartDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Cart.objects.all()
    serializer_class= CartSerializer
    name= 'cart-detail'
    permission_classes=(  
        custompermission.Isowner,
    )

class ItemsFilter(filters.FilterSet):

    class Meta:
        model= Items
        fields = (
            'name',
            )

class ItemsList(generics.ListCreateAPIView):
    throttle_scope= 'items'
    throttle_classes= (ScopedRateThrottle,)
    queryset= Items.objects.all()
    serializer_class= ItemSerializer
    name= 'items-list'
    filterset_class= ItemsFilter
    ordering_fields=('name',)
    search_fields= ['name','price', 'item_category',]
    

class ItemsDetail(generics.RetrieveUpdateDestroyAPIView):
    throttle_scope= 'items'
    throttle_classes= (ScopedRateThrottle,)
    queryset= Items.objects.all()
    serializer_class= ItemSerializer
    name= 'items-detail'
    

class OrderList(generics.ListCreateAPIView):
    queryset= Order.objects.all()
    serializer_class= OrderSerializer
    name= 'order-list'
    search_fields=['items', 'total_price', ]
    permission_classes=(
        permissions.IsAuthenticatedOrReadOnly,
    )
    def perform_create(self, serializer): 
        serializer.save(owner=self.request.user.profile)

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset= Order.objects.all()
    serializer_class= OrderSerializer
    name= 'order-detail'
    permission_classes=(
        permissions.IsAuthenticatedOrReadOnly,
        custompermission.Isowner,
    )
    

class ApiRoot(generics.GenericAPIView):
    name= 'api-root'
    def get(self, request, *args, **kwargs,):
        return Response({
            'profile': reverse(ProfileList.name, request=request),
            'Stores': reverse(Storelist.name, request=request),
            'Category': reverse(Categorylist.name, request=request),
            'Items': reverse(ItemsList.name, request=request),
            'Carts': reverse(CartList.name, request=request),
            'Orders': reverse(OrderList.name, request=request)
        })
        