from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import main_page, comment
from .forms import ProductForms, CommentForm
from django.views.decorators.http import require_http_methods, require_POST
from django.shortcuts import get_object_or_404

# Create your views here.
@login_required
def product_page(request):
    products = main_page.objects.all().order_by('-created_at')
    context = {
        'products' : products
    }
    return render(request, 'product/product_page.html', context)

@login_required
def new_product(request):
    if request.method == 'POST':
        form = ProductForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product:product_page')
    else:
        form = ProductForms()
        context = {
            'form' : form
        }
    return render(request, 'product/new_product.html', context)

@login_required
def save_product(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    image = request.FILES.get('image')
    new_product = main_page.objects.create(title=title, content=content, image = image)
    return redirect("product:product_detail", new_product.id)

@login_required
def product_detail(request, pk):
    new_product = main_page.objects.get(pk=pk)
    form = ProductForms(instance = new_product)
    comment_form = CommentForm()
    comments = new_product.comments.all().order_by('-pk')
    context = {
        "new_product": new_product, 
        'form':form, 
        'comment_form' : comment_form, 
        'comments' : comments
    }
    return render(request, "product/product_detail.html", context)

@login_required
def delete(request, pk):
    product = main_page.objects.get(pk=pk)
    product.delete()
    return redirect("product:product_page")


@login_required
def delete_prod(request, pk):
    del_product = main_page.objects.get(pk=pk)
    context = {'del_product' : del_product}
    return render(request, 'product/delete_prod.html', context)

@require_http_methods(['GET', 'POST'])
@login_required
def edit_prod(request, pk):
    edit_prod = main_page.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProductForms(request.POST, files = request.FILES, instance = edit_prod)
        if form.is_valid():
            form.save()
            return redirect('product:product_detail', pk)
    else:
        form = ProductForms(files = request.FILES, instance = edit_prod)
        context = {'edit_prod' : edit_prod, 'form' : form}
    return render(request, 'product/edit_prod.html', context)


@login_required
@require_POST
def comments(request, pk):
    article = get_object_or_404(main_page, pk = pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.article = article
        comment.save()
        return redirect('product:product_detail', pk)
        
    
    