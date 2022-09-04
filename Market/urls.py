
from django.urls import re_path, path
from Market import views 
from User import views as uviews

urlpatterns = [ 
    re_path(r'^profile/$', uviews.ProfileList.as_view(),
        name= uviews.ProfileList.name),
    path('profile/<str:pk>/', uviews.ProfileDetail.as_view(),
        name= uviews.ProfileDetail.name),
    re_path(r'^stores/$', views.Storelist.as_view(),
        name= views.Storelist.name),
    re_path(r'^stores/(?P<pk>[0-9]+)$', views.StoreDetail.as_view(),
        name=views.StoreDetail.name),
    re_path(r'^items-categories/$', 
        views.Categorylist.as_view(), 
        name=views.Categorylist.name), 
    re_path(r'^items-categories/(?P<pk>[0-9]+)$', 
        views.Categorydetail.as_view(), 
        name=views.Categorydetail.name), 
    re_path(r'^items/$', 
        views.ItemsList.as_view(), 
        name=views.ItemsList.name), 
    re_path(r'^items/(?P<pk>[0-9]+)$', 
        views.ItemsDetail.as_view(), 
        name=views.ItemsDetail.name), 
    re_path(r'^orders/$', 
        views.OrderList.as_view(), 
        name=views.OrderList.name), 
    re_path(r'^orders/(?P<pk>[0-9]+)$', 
        views.OrderDetail.as_view(), 
        name=views.OrderDetail.name), 
    re_path(r'^carts/$', 
        views.CartList.as_view(), 
        name=views.CartList.name), 
    re_path(r'^carts/(?P<pk>[0-9]+)$', 
        views.CartDetail.as_view(), 
        name=views.CartDetail.name), 
    re_path(r'^$', 
        views.ApiRoot.as_view(), 
        name=views.ApiRoot.name), 
    ]