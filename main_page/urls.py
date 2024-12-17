from django.contrib import admin
from django.urls import include, path
from . import views

app_name = 'product'
urlpatterns = [
    path('', views.product_page, name = 'product_page'),
    path('new_product/', views.new_product, name = 'new_product'),
    path('save_product/', views.save_product, name = 'save_product'),
    path('<int:pk>/', views.product_detail, name = 'product_detail'),
    path("<int:pk>/delete/", views.delete, name="delete"),
    path("<int:pk>/delete/delete_prod/", views.delete_prod, name = 'delete_prod'),
    path("<int:pk>/edit_prod/", views.edit_prod, name="edit_prod"),
    path("<int:pk>/comments", views.comments, name = 'comments'),
]

