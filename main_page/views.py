from django.shortcuts import render, redirect

# Create your views here.
def product_page(request):
    return render(request, 'product_page.html')