from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.product_page, name = 'product_page'),
    path('new_product/', views.new_product, name = 'new_product')
]
